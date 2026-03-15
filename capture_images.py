import os
import uuid
import time
import cv2
import matplotlib.pyplot as plt
import numpy as np

IMAGE_PATH = os.path.join('data', 'images')
number_images = 1

cap = cv2.VideoCapture(0)
for imgnum in range(number_images):
    print('Collecting image {}'.format(imgnum))
    ret, frame = cap.read()
    if ret and frame is not None:
        imgname = os.path.join(IMAGE_PATH, f'{str(uuid.uuid1())}.jpg')
        cv2.imwrite(imgname, frame)
        # Image is saved, no display
    else:
        print('Failed to capture image.')
    time.sleep(0.5)
cap.release()