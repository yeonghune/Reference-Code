import dlib
import os
import cv2

detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture('Video/video.avi')
cnt = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret :
        print("CAM NOT OPEND")
        break
    frame = cv2.flip(frame,0)
    faces = detector(frame)
    for face in faces:
        save_img = frame[face.top():face.bottom(),face.left():face.right()]
        really_save_img = cv2.resize(save_img, dsize=(224,224),interpolation=cv2.INTER_AREA)
        cv2.imwrite('Videoresult/{0}.jpg'.format(cnt), really_save_img)
        cnt +=1
cap.relase()