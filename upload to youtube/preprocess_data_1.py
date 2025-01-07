import pandas as pd
import math
import numpy as np

path_to_csv_file = r'path_to_csv_file'

# Converting CSV to String for making QR easily
df = pd.read_csv(path_to_csv_file)
data_row = ''
for row in df.itertuples():
    data_row += str(list(row))

# Breaking string into lists of length 2000
data_array = []
data_length = 2000
temp = 0
for index, letter in enumerate(data_row):
    if index%data_length == 0 and index != 0:
        data_array.append(data_row[temp:index])
        temp = index
data_array.append(data_row[temp:])

# Logic for counting words
counter = 0
for arr in data_array:
    for word in arr:
        counter += 1

np.save('./temporary/data_array.npy', data_array)

print(f'Total QR codes : {len(data_array)}')    
print(f'Total time of video : { len(data_array)/30 if len(data_array)/30 < 1 else math.ceil(len(data_array)/30)}')
print(f'Total words : {counter}')
print(f'Estimated size for total QR codes : {(len(data_array)*475)//1000}')

print('\n\n------Done with Preprocessing step------')