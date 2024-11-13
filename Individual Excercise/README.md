# YOLOv8 Soda Can Detection
This project uses a video feed and a YOLOv8 model to detect soda cans in real time. The program uses the ultralytics package for object recognition using YOLO and OpenCV for video recording and display.

## You will need 
- Python 
- OpenCV 
- Ultralytics YOLO

## How to use it
1. Ensure the YOLO model file (best.pt) is available in the same directory. 

2. Run the script directly from visual studio or similar or with: python cam.py

3. The script will open a camera feed and continuously detect objects, in this case, soda cans, in real-time.
  
4. Lastly, press q to close the camera feed and exit the program.

## Configuration
- The  camera ID is set to 1. Modify the cam_id parameter in the detection function if a different camera is needed.
- The confidence threshold for detections is set to 0.8 to avoid false positives. 

## Project Structure
- cam.py: Main script for running real-time soda can detection using YOLOv8.
- best.pt: YOLO model to detect soda cans.
  * Model was trained using Roboflow
  * Background images with no soda cans were added to avoid false positives.

