import os
from googleapiclient.discovery import build
import json

class Video:
    def __init__(self, video_id: str) -> None:
        #self._channel_id = channel_id  # HighLoad Channel

        #self.base_url = 'https://www.googleapis.com/youtube/v3/channels'
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        self.api_key: str = os.environ.get("API_YUTUBE_KEY")
        # создать специальный объект для работы с API
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        #self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        #self.title = self.channel["items"][0]["snippet"]["title"]
        #self.description = self.channel["items"][0]["snippet"]["description"]
        #self.url = 'https://www.youtube.com/channel/' + self._channel_id
        #self.subscriberCount = self.channel["items"][0]["statistics"]["subscriberCount"]
        #self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        #self.viewCount = self.channel["items"][0]["statistics"]["viewCount"]

        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
       # self.video_title: str = self.video_response['items'][0]['snippet']['title']
       # self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
       # self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
       # self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']


def __str__(self):
        return f'({self.base_url} )'

class PLVideo(Video):
    def __init__(self, channel_id, video_id) -> None:
        super().__init__(channel_id)
        self.video_id = video_id