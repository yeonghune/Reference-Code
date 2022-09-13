import dlib
import os
import cv2

photo_path = 'photo'
save_path = 'result'
detector = dlib.get_frontal_face_detector()



for image_name in os.listdir(photo_path):
    cnt = 0
    ex_image_path = os.path.join(photo_path,image_name)
    for image_path in os.listdir(ex_image_path):
        image_path = os.path.join(ex_image_path,image_path)
        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
        
        faces = detector(img, 0)
        for face in faces:
            save_img = img[face.top():face.bottom(),face.left():face.right()]
            really_save_img = cv2.resize(save_img, dsize=(224,224),interpolation=cv2.INTER_AREA)
            really_save_path = os.path.join(save_path,image_name)
            really_really_save_path = os.path.join(really_save_path,'{0}.jpg'.format(cnt))
            
        if os.path.exists(really_save_path) == False:
            os.makedirs(really_save_path)
        
        cv2.imwrite(really_really_save_path,really_save_img)
        cnt += 1
