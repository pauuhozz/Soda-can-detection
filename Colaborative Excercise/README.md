# YOLOv8 Soda Can Detection
This project uses a video feed and a YOLOv8 model to detect objects. There were two options, to detect spoons or to detect soda cans in real time. It was decided to use the soda can recognition. The program uses the ultralytics package for object recognition using YOLO and OpenCV for video recording and display.

## You will need 
- Python 
- OpenCV 
- Ultralytics YOLO

## How to use it
1. Ensure the YOLO model file (best.pt) is available in the same directory. 

2. Run the script directly from visual studio or similar or with: python cam.py

3. The script will open a camera feed.

4. Press p to analyze the image. Press q to close the annotated image. Repeat this step as many times as needed.
  
4. Lastly, press q to close the camera feed and exit the program.

## Configuration
- The  camera ID is set to 1. Modify the cam_id parameter in the detection function if a different camera is needed.
- The confidence threshold for detections is set to 0.8 to avoid false positives. 

## Project Structure
- client.py: Client script for running soda can detection using YOLOv8.
- Server.py: Server script to received and print the coordinates of the top mostleft soda can.
- TestSampleImages: This program was added for reviewing purposes. This program works the same as the client program, but instead of using a live webcam, images are directly loaded. These images are available in the same folder. Also, socket connection was commented to make the reviewing easier. 
- best.pt: YOLO model to detect soda cans.
  * Model was trained using Roboflow: https://app.roboflow.com/erasmus-eo69k/soda-cans-vivjo/2
  * Background images with no soda cans were added to avoid false positives.


!! A video to proof the program working can be found on the folder (Leftmost object coordinates.mp4)