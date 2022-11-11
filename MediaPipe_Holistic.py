#import Libraries
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic

# For webcam input:
cap = cv2.VideoCapture(0) #To change camera capture you have to change the number

with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        success, image = cap.read()
        w = image.shape[0]
        h = image.shape[1]
        
        
