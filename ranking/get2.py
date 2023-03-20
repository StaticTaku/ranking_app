import google.auth
from googleapiclient.discovery import build

# Google Cloud Consoleで取得したAPIキーを設定
API_KEY = 'AIzaSyDFdBMczCViKNoHai7oKKtLgjJloAzAsrQ'

# YouTube Data APIを使用するためのサービスオブジェクトを作成
youtube = build('youtube', 'v3', developerKey=API_KEY)

# 取得したい再生リストのIDを設定
PLAYLIST_ID = 'RDCLAK5uy_nVjU2j4lOFyJicLDWEMjYmBkaejmrsx5M'

# 再生リスト内の動画の情報を取得するためのリクエストオブジェクトを作成
request = youtube.playlistItems().list(
    part='snippet',
    playlistId=PLAYLIST_ID,
    maxResults=50 # 一度に取得できる最大件数（デフォルトは5）
)

# リクエストオブジェクトからレスポンスオブジェクトを取得
response = request.execute()

# レスポンスオブジェクトから動画の情報を抽出して表示
for item in response['items']:
    # 動画ID
    video_id = item['snippet']['resourceId']['videoId']
    # 動画タイトル
    video_title = item['snippet']['title']
    # 動画説明文
    #video_description = item['snippet']['description']
    # 動画サムネイルURL
    video_thumbnail_url = item['snippet']['thumbnails']['default']['url']

    print(f'ID: {video_id}')
    print(f'Title: {video_title}')
    #print(f'Description: {video_description}')
    print(f'Thumbnail URL: {video_thumbnail_url}')

    print('\n\n')