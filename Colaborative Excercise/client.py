# This is the original version. The code is designed to run on a live feed from a camera. 

import cv2
import socket
from ultralytics import YOLO

def detection(model, cam_id=1, host='192.168.0.107', port=5000):
    # Load the YOLOv8 model
    yoloModel = YOLO(model)
    
    # Start the video capture
    cam = cv2.VideoCapture(cam_id)
    if not cam.isOpened():
        print("Could not open the camera.")
        return

    print("Press 'p' to take a picture and analyze it. Press 'q' to exit.")
    
    # Set up client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            # Read the current frame
            ret, frame = cam.read()
            if not ret:
                print("Error capturing frame.")
                break

            # Display the live camera feed
            cv2.imshow("Live Feed - Press 'p' to analyze", frame)

            # Wait for key press
            key = cv2.waitKey(1) & 0xFF

            # If 'p' is pressed, capture the frame for analysis
            if key == ord('p'):
                # Detect objects in the captured frame
                results = yoloModel(frame, conf=0.8)

                # Check if any objects are detected
                if results[0].boxes:
                    # Initialize the top-left box and minimum x, y values
                    top_left_box = None
                    min_x, min_y = float('inf'), float('inf')

                    # First, find the box with the smallest x-coordinate, then y-coordinate 
                    for box in results[0].boxes:
                        x1, y1, x2, y2 = box.xyxy[0].int().tolist()
                        
                        # Update top-left box based on x, and then y if x is the same
                        if (x1 < min_x) or (x1 == min_x and y1 < min_y):
                            min_x, min_y = x1, y1
                            top_left_box = (x1, y1)

                    if top_left_box:
                        x, y = top_left_box
                        coordinates = f"{x},{y}"
                        
                        # Send the coordinates to the server
                        client_socket.sendall(coordinates.encode())

                        # Print coordinates to confirm
                        print("Sent coordinates:", coordinates)

                # Draw the annotations on the frame
                annotatedFrame = results[0].plot()
                
                # Show the frame with the annotations in a new window
                cv2.imshow("Detection Result", annotatedFrame)
                cv2.waitKey(0)  # Wait for any key press to close this window
                cv2.destroyWindow("Detection Result")

            # Exit if the user presses 'q'
            elif key == ord('q'):
                break
    finally:
        # Free the resources
        cam.release()
        cv2.destroyAllWindows()
        client_socket.close()
        print("Client connection closed.")

# Run the detection with server communication
detection('best.pt')