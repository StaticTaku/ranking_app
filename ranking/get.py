import google.auth
from googleapiclient.discovery import build

# Google Cloud Consoleで取得したAPIキーを設定
API_KEY = 'AIzaSyDFdBMczCViKNoHai7oKKtLgjJloAzAsrQ'

# YouTube Data APIを使用するためのサービスオブジェクトを作成
youtube = build('youtube', 'v3', developerKey=API_KEY)

# 取得したい動画のIDを指定
video_id = 'v2coP8GtTTI'

# 動画のタイトルとサムネイルを取得
"""
video_info = youtube.videos().list(
    part='snippet',
    id=video_id
).execute()
"""

search_response = youtube.search().list(
    q='JPOP',
    type='video',
    part='id,snippet',
    maxResults=32
).execute()

for search_result in search_response.get('items', []):
    print(f"Title: {search_result['snippet']['title']}")
    print(f"Video ID: {search_result['id']['videoId']}")
    print(f"Channel: {search_result['snippet']['channelTitle']}\n")

"""
title = video_info['items'][0]['snippet']['title']
thumbnail_url = video_info['items'][0]['snippet']['thumbnails']['default']['url']

print(title)
print(thumbnail_url)
"""