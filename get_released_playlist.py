"""load django"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()
"""complete loading"""


"""script start"""
import google.auth
from googleapiclient.discovery import build
from ranking.models import MovieTournament
import datetime
dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
# Google Cloud Consoleで取得したAPIキーを設定
API_KEY = 'AIzaSyDFdBMczCViKNoHai7oKKtLgjJloAzAsrQ'

# YouTube Data APIを使用するためのサービスオブジェクトを作成
youtube = build('youtube', 'v3', developerKey=API_KEY)

# released play list
PLAYLIST_ID = 'PLOHoVaTp8R7dfrJW5pumS0iD_dhlXKv17'

# 再生リスト内の動画の情報を取得するためのリクエストオブジェクトを作成
playlist_items = []
request = youtube.playlistItems().list(
    part='snippet',
    playlistId=PLAYLIST_ID,
    maxResults=50 # 一度に取得できる最大件数（デフォルトは5）
)

# リクエストオブジェクトからレスポンスオブジェクトを取得
response = request.execute()
playlist_items += response['items']

# 次のページがあれば、ページングしながらplaylistItemsを取得
while 'nextPageToken' in response:
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=PLAYLIST_ID,
        maxResults=50,
        pageToken=response['nextPageToken']
    )
    response = request.execute()
    playlist_items += response['items']


new_object = MovieTournament()
new_object.name = f"KPOP 2023 - K-POP Songs 2023"
new_object.comment = f"今はやりのKPOPでトーナメント！"
new_object.category = "music"

link_list  = []
title_list = []
# レスポンスオブジェクトから動画の情報を抽出して表示
for item in playlist_items:
    # 動画ID
    video_id = item['snippet']['resourceId']['videoId']
    link_list.append(video_id)

    # 動画タイトル
    video_title = item['snippet']['title']
    
    title_list.append(video_title.replace(",", " "))
    # 動画説明文
    #video_description = item['snippet']['description']
    # 動画サムネイルURL
    #video_thumbnail_url = item['snippet']['thumbnails']['default']['url']

new_object.link_list = link_list
new_object.title_list = title_list
new_object.save()
