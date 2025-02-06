import pandas as pd
import numpy as np
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import os
import base64

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
vid_path = r'path_to_video'
csv_name = os.listdir('./temporary')[-1].split('.')[0]

cap = cv2.VideoCapture(vid_path)
result = b''
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
        decoded_bytes = base64.b64decode(data)
        print(f"Decoded bytes of length : {len(decoded_bytes)}")
        result += decoded_bytes
        
output_file = r'output_file_path'
with open(output_file, "wb") as f:
    f.write(result)

print(f"\n\n------CSV files saved at path : ../outputs/{csv_name}.csv------")