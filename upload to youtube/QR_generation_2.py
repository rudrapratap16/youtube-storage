import qrcode
import pandas as pd
import cv2
import random
import os
from pyzbar.pyzbar import decode
from PIL import Image
import math
import numpy as np

data_array = np.load('./temporary/data_array.npy')

def make_qr(index, ele):
    qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(data=ele)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'./temporary/output_{index}.png')

    image = cv2.imread(f'./temporary/output_{index}.png')
    image = cv2.resize(image, (1080, 1080))
    cv2.imwrite(f'./temporary/output_{index}.png', image)
    # image.save(f'./output/output_{index}.png')

for index, ele in enumerate(data_array):
    make_qr(index, ele)
    print(f"Done with : output_{index}.png")


print('\n\n------Done with QR Generation step------')