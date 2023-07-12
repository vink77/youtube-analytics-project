import os
from googleapiclient.discovery import build
import json


class Video:
    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        # API_YUTUBE_KEY скопирован из гугла и вставлен в переменные окружения
        self.api_key: str = os.environ.get("API_YUTUBE_KEY")
        # создать специальный объект для работы с API
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        try:
            self.video_response = self.youtube.videos().list(part='snippet,statistics', id=video_id).execute()
            self.title = self.video_response['items'][0]['snippet']['title']
            self.url = 'https://www.youtube.com/channel/' + video_id
            self.view_count = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count = self.video_response['items'][0]['statistics']['likeCount']
        except (Exception):
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id, playlist_id) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id
