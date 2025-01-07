import yt_dlp

SAVE_PATH = "./temporary/"  # Update the path where you want to save the video
link = "https://www.youtube.com/shorts/MA4F9atmuus"

ydl_opts = {
    'format': 'best',
    'outtmpl': f'{SAVE_PATH}%(title)s.%(ext)s',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Video downloaded successfully!')
except Exception as e:
    print(f"Some Error! {e}") 
