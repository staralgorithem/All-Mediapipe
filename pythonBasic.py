#import Libraries
import cv2
import mediapipe

#Modules
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

# For webcam input:
capture = cv2.VideoCapture(0)


with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:
 
    while (True):
 
        ret, frame = capture.read()
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
 
