import pandas as pd
import math
import numpy as np
import qrcode
import cv2
import base64

path_to_csv_file = "path to file"

def make_qr(ele):
    qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(data=ele)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Get image in PIL format
    pil_img = img.get_image()

    # Converting to cv2 image and resizing it
    cv_img = pil_img.convert('RGB')
    image = np.array(cv_img)
    image = cv2.resize(image, (1080, 1080))
    return image

chunk_size = 1000 # 1 KiB
qr_images = []
data = 0
with open(path_to_csv_file, "rb") as in_file:
    while True:
        chunk = in_file.read(chunk_size)
            
        if chunk == b"":
            break # end of file
        chunk = base64.b64encode(chunk).decode('utf-8')
        qr = make_qr(chunk)
        qr_images.append(qr)

print("\n\n------Done with making arrays------\n\n")

# Video Creation Part   
start_buffer_folder = './buffers/start'
end_buffer_folder = './buffers/end'
video_name = './temporary/video.avi'

# Creating array by joining values of each frame
images = []
for i in range(60):
    images.append(cv2.imread(f'{start_buffer_folder}/start_buffer_0.png'))
images.extend(qr_images)
for i in range(60):
    images.append(cv2.imread(f'{end_buffer_folder}/end_buffer_0.png'))

frame = images[0]
height, width, layers = frame.shape

# Initializing video writer and setting it to 30 fps
video = cv2.VideoWriter(video_name, 0, 30, (width,height))

print("Processing Video...")

# Joining images frame by frame to create video
for image in images:
    video.write(image)

cv2.destroyAllWindows()
video.release()

print(f"Made video at location : {video_name}")
print("\n\n------Done with making video using arrays------\n\n")