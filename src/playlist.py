import datetime, isodate, os
from datetime import timedelta
from googleapiclient.discovery import build


class PlayList:
    def __init__(self, playlist_id):
        self.api_key: str = os.environ.get("API_YUTUBE_KEY")
        #  специальный объект для работы с API
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.playlist_id = playlist_id
        """получить данные по видеороликам в плейлисте"""
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()

        self.playlist = self.youtube.playlists().list(id=playlist_id,
                                                      part='snippet',
                                                      maxResults=50,
                                                      ).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"
        # получить все id видеороликов из плейлиста
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        # получить статистику видео по его id
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                         id=','.join(self.video_ids)
                                                         ).execute()

    @property
    def total_duration(self):
        """возвращает объект класса datetime.timedelta с суммарной длительность плейлиста
        (обращение как к свойству, использовать @ property)"""
        delta = 0
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            duration = isodate.parse_duration(video['contentDetails']['duration'])
            delta += (timedelta.total_seconds(duration))
        return datetime.timedelta(seconds=delta)

    def show_best_video(self):
        """возвращает ссылку на самое популярное видео из плейлиста(по количеству лайков)"""
        max_like = self.video_response['items'][0]['statistics']['likeCount']
        for item in self.video_response['items']:
            if item['statistics']['likeCount'] > max_like:
                max_like = item['statistics']['likeCount']
                max_id = item['id']
        return f'https://youtu.be/{max_id}'

