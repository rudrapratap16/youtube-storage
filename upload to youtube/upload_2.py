from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Scopes required for uploading videos
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate(path_for_cred):
    # Load credentials from the saved JSON file
    creds = Credentials.from_authorized_user_file(path_for_cred, SCOPES)
    return creds

def upload_video(credentials, video_file, title, description, category_id, tags):
    # Build the YouTube client
    youtube = build('youtube', 'v3', credentials=credentials)

    # Prepare the video metadata
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': 'public'
        }
    }

    # Attach the video file
    media = MediaFileUpload(video_file, resumable=True)

    # Make the API request to upload the video
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = request.execute()
    print("Upload successful! Video ID:", response["id"])

path_for_cred = './credentials/youtube_cred.json'

creds = authenticate(path_for_cred)

# Set your video details here
video_path = "./temporary/video.avi"                                                        # Replace with your video file name
video_title = video_path.split('/')[-1].split('.')[0] if '/' in video_path else video_path.split('.')[0]  # Replace with your video title
video_description = f"Data of : {video_title}"                                # Replace with your video description
video_category_id = "22"                                                      # Replace with the category ID
video_tags = ["example", "tags", "youtube"]                                   # Replace with relevant tags

# Upload the video
upload_video(creds, video_path, video_title, video_description, video_category_id, video_tags)

print(f"\n\n------Video uploaded on youtube using your credentials titled : {video_title}------")
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Scopes required for uploading videos
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate(path_for_cred):
    # Load credentials from the saved JSON file
    creds = Credentials.from_authorized_user_file(path_for_cred, SCOPES)
    return creds

def upload_video(credentials, video_file, title, description, category_id, tags):
    # Build the YouTube client
    youtube = build('youtube', 'v3', credentials=credentials)

    # Prepare the video metadata
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': 'public'
        }
    }

    # Attach the video file
    media = MediaFileUpload(video_file, resumable=True)

    # Make the API request to upload the video
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = request.execute()
    print("Upload successful! Video ID:", response["id"])

path_for_cred = './credentials/youtube_cred.json'

creds = authenticate(path_for_cred)

# Set your video details here
video_path = "./temporary/video.avi"                                                        # Replace with your video file name
video_title = video_path.split('/')[-1].split('.')[0] if '/' in video_path else video_path.split('.')[0]  # Replace with your video title
video_description = f"Data of : {video_title}"                                # Replace with your video description
video_category_id = "22"                                                      # Replace with the category ID
video_tags = ["example", "tags", "youtube"]                                   # Replace with relevant tags

# Upload the video
upload_video(creds, video_path, video_title, video_description, video_category_id, video_tags)

print(f"\n\n------Video uploaded on youtube using your credentials titled : {video_title}------")