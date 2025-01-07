import os

for file in os.listdir('./download and decode/temporary/'):
    os.remove(f'./download and decode/temporary/{file}')
for file in os.listdir('./upload to youtube/temporary/'):
    os.remove(f'./upload to youtube/temporary/{file}')