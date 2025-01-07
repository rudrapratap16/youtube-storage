import qrcode
import pandas as pd
import cv2
import random
import os
from pyzbar.pyzbar import decode
from PIL import Image
import math


start_buffer_folder = './buffers/start/'
end_buffer_folder = './buffers/end/'
image_folder = './temporary/'
video_name = './temporary/video.avi'

# Array to contain the names of files for each frame
images = []
for i in range(60):
    images.append(f'start_buffer_0.png')
for i in range(len(os.listdir(image_folder))-1):
    images.append(f'output_{i}.png')
for i in range(60):
    images.append(f'end_buffer_0.png')

# Making video
frame = cv2.imread(os.path.join(start_buffer_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (width,height))

for image in images:
    if image[:12] == 'start_buffer':
        video.write(cv2.imread(os.path.join(start_buffer_folder, image)))
    elif image[:10] == 'end_buffer':
        video.write(cv2.imread(os.path.join(end_buffer_folder, image)))
    else:
        video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

print(f"Made video at location : {video_name}")
print("\n\n------Done with making video using images------")