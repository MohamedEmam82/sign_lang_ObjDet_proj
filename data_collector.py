'''
take images for the different labels from laptop camera 
and save every image in it's label/category folder
'''

import os
import cv2
import time
import uuid  # create unique id for a file


IMAGE_PATH = "CollectedImages"

labels = ['Hello', "Yes", "No", "Thanks", "ILoveYou", "Please"]
number_of_images = 5  # for every label of the labels list..should be at least 500 images in real project for high performance

delay1 = 5
delay2 = 3
for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)

    # open camera
    cap = cv2.VideoCapture(0) # 0 -> select the default camera
    print(f"Collecting images for {label} after {delay1} sec...")
    time.sleep(delay1)
    print(f"START....")

    for imgnum in range(number_of_images):
       ret, frame =  cap.read()   # ret = does frame exist? -> (True/False),    frame = video frames
       imagename = os.path.join(IMAGE_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
       cv2.imwrite(imagename, frame)
       cv2.imshow('frame', frame)

       print(f" {label} image # {imgnum+1} captured...prepare foe next one after {delay2} sec...")
       time.sleep(delay2)
       
       # exit the camera when a key is preesed & this key is 'q'
        # ord() function returns the number representing the unicode code of a specified character.
        # char() does the vice versa
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
        
    cap.release()

