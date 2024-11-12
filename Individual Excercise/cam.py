import cv2
from ultralytics import YOLO

def detection(model, cam_id=1):
    # Load the YOLOv8 model
    yoloModel = YOLO(model)
    
    # Start the video capture
    cam = cv2.VideoCapture(cam_id)
    if not cam.isOpened():
        print("Could not open the camera.")
        return

    print("Press q to exit.")
    
    while True:
        # Read the current frame
        ret, frame = cam.read()
        if not ret:
            print("Error capturing frame.")
            break

        # Detect objects in the frame
        results = yoloModel(frame, conf = 0.8)
        
        # Draw the annotations on the frame
        annotatedFrame = results[0].plot()
        
        # Show the frame with the annotations
        cv2.imshow("Detecting: ", annotatedFrame)

        # Exit if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Free the resources
    cam.release()
    cv2.destroyAllWindows()

detection('best.pt')
