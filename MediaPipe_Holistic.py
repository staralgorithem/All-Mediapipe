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
        
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)

        # Draw landmark annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.pose_landmarks:
        
            # for index, landmark in enumerate(results.pose_landmarks.landmark):
            #     # val = results.pose_landmarks;
            #     # num = len(results.pose_landmarks.landmark);
            #     print("index : " + str(index) + " x: "+ str(landmark.x) + " y: "+ str(landmark.y) + " z: "+ str(landmark.z));
            #     # print(val)
            # index = 8
            # print("['INDEX'] -- " + "index : " + str(index) + " x: "+ str(results.left_hand_landmarks.landmark[index].x) + " y: "+ str(results.left_hand_landmarks.landmark[index].y));
            # pos = (int(results.left_hand_landmarks.landmark[index].x*h),int(results.left_hand_landmarks.landmark[index].y*w))
            # print(pos)
            # cv2.circle(image,pos,20,(255,0,0),-1)
            
            print("data :" + str(results.pose_landmarks.landmark))
