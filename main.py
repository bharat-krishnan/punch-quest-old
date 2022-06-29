# 3rd Party Libraries
import cv2
import torch
from mediapipe import solutions as mp

# Custom Libraries
from sort import *

# Import YOLOv5n (smallest model) for object dection, only include human detection
model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True) 
model.classes=[0]

# Import Mediapipe pose detection model and drawing utilities
mp_drawing = mp.drawing_utils
mp_pose = mp.pose


# Set the video that is to be captured (0 = webcam, path = video)
vid = cv2.VideoCapture('testVideos/spar.mov')
# vid = cv2.VideoCapture(0)
# vid = cv2.VideoCapture('testVideos/exampleFootage.mp4')

# Create tracker object to keep tracking specific human objects accross frame
mot_tracker = Sort()

# Global Variables
MARGIN = 10
WHITE = (255,255,255)
RED = (0,0,255)
BLUE = (255,0,0)

# Go through video frame by frame for analysis
with mp_pose.Pose(min_detection_confidence=0.3, min_tracking_confidence=0.3) as pose:
    while vid.isOpened():

        # Get frame
        ret, frame = vid.read()

        # Recolor frame from RGB to BGR & make image unwriteable to improve prediction
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False   

        # Make human detection prediction and update tracker accordingly
        preds = model(image)
        detections = preds.pred[0].numpy() 
        track_bbs_ids = mot_tracker.update(detections)

        # Recolor image back to BGR for rendering & make image writeable again
        image.flags.writeable = True   
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Go through all items being tracked
        for j in range(len(track_bbs_ids.tolist())):

            # Get the coordinates of their bounding box and deconstruct them
            coords = track_bbs_ids.tolist()[j] 
            x1, y1, x2, y2 = int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])

            # Get specific human ID and create a label for them
            name_idx = int(coords[4])
            name = "ID : {}".format(str(name_idx)) 
            color = RED

            # Get pose results and draw them onto humans
            results = pose.process(image[int(y1)+MARGIN:int(y2)+MARGIN,int(x1)+MARGIN:int(x2)+MARGIN:])
            mp_drawing.draw_landmarks(
                    image[int(y1)+MARGIN:int(y2)+MARGIN,int(x1)+MARGIN:int(x2)+MARGIN:], 
                    results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=RED, thickness=2, circle_radius=2), 
                    mp_drawing.DrawingSpec(color=WHITE, thickness=2, circle_radius=2) 
                    ) 

            # Draw bounding box of human w/ label
            cv2.rectangle(image, (x1, y1),(x2,y2), color, 2)
            cv2.putText(image, name, (x1, y1-10), cv2.FONT_HERSHEY_DUPLEX, 0.9, color, 2) 



            # Display new image
            cv2.imshow('Image', image) 
        
        # Emergency Break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 

# After the loop release the video object
vid.release()
# Destroy all the windows 
cv2.destroyAllWindows()