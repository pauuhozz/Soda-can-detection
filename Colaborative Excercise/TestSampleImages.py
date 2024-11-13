import cv2
# import socket
from ultralytics import YOLO

def detection(model, image_path, host='192.168.0.107', port=5000):
    # Load the YOLOv8 model
    yoloModel = YOLO(model)
    
    # Try to load the image
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Could not load the image at {image_path}")
        return

    print("Press 'p' to analyze the image or 'q' to exit.")

    # Client socket configuration
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect((host, port))

    try:
        while True:
            # Display the image in a window
            cv2.imshow("Image - Press 'p' to analyze", frame)

            # Wait for the user to press a key
            key = cv2.waitKey(1) & 0xFF

            # If 'p' is pressed, analyze the image
            if key == ord('p'):
                # Detect objects in the image
                results = yoloModel(frame, conf=0.8)

                # Check if objects were detected
                if results[0].boxes:
                    # Initialize the top-left box and minimum x, y values
                    top_left_box = None
                    min_x, min_y = float('inf'), float('inf')

                    # Find the box with the smallest x and y coordinates
                    for box in results[0].boxes:
                        x1, y1, x2, y2 = box.xyxy[0].int().tolist()
                        
                        # Update the top-left box based on x, y
                        if (x1 < min_x) or (x1 == min_x and y1 < min_y):
                            min_x, min_y = x1, y1
                            top_left_box = (x1, y1)

                    if top_left_box:
                        x, y = top_left_box
                        coordinates = f"{x},{y}"
                        
                        # Send coordinates to the server
                        # client_socket.sendall(coordinates.encode())

                        # Confirm the coordinates sent
                        print("Sent coordinates:", coordinates)

                # Draw annotations on the image
                annotatedFrame = results[0].plot()
                
                # Show the image with annotations in a new window
                cv2.imshow("Detection Result", annotatedFrame)
                cv2.waitKey(0)  # Wait until any key is pressed to close this window
                cv2.destroyWindow("Detection Result")

            # Exit if 'q' is pressed
            elif key == ord('q'):
                break
    finally:
        # Release resources
        cv2.destroyAllWindows()
        # client_socket.close()
        print("Client connection closed.")

# Run detection with server communication
detection('best.pt', 'image2.jpeg')
