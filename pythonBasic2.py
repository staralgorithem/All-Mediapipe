#Import Libraries
import mediapipe as mp
import cv2

# Drawing/ Kolistics
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Capture
cap = cv2.VideoCapture(0)
# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        ret, frame = cap.read()
