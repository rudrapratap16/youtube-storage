import pandas as pd
import numpy as np
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import os

def read_qr(frame):
    
    image = Image.fromarray(frame)
    decoded_objects = decode(image)

    if decoded_objects:
        for obj in decoded_objects:
            return obj.data.decode('utf-8')
    else:
        print("No QR Code detected.")
        return None

vid_path = f"./temporary/{os.listdir('./temporary/')[-1]}"
csv_name = os.listdir('./temporary')[-1].split('.')[0]

cap = cv2.VideoCapture(vid_path)
result = ''
counter = 0
while cap.isOpened():
    ret, frame = cap.read()
    counter += 1
    if not ret:
        print("Can't receive frame. Exiting ...")
        print(counter)
        break
    data = read_qr(frame)
    if data == 'start buffer' or data == 'end buffer':
        continue
    else:
        result += data
        
start_pos = 0
with open(f'../outputs/{csv_name}.csv', 'w') as file:
    for index, letter in enumerate(result):
        if letter == '[':
            start_pos = index
        elif letter == ']':
            file.write(result[start_pos+1:index]+'\n')
    
print(f"\n\n------CSV files saved at path : ../outputs/{csv_name}.csv------")