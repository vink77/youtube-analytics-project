import os
from googleapiclient.discovery import build
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.base_url = 'https://www.googleapis.com/youtube/v3/channels'
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        self.api_key: str = os.environ.get("API_YUTUBE_KEY")
        # создать специальный объект для работы с API
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.__channel_id = channel_id  # HighLoad Channel
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subscriberCount = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.viewCount = self.channel["items"][0]["statistics"]["viewCount"]

    def __str__ (self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other):
        return int(self.subscriberCount) - int(other.subscriberCount)

    def __gt__(self, other):
        return int(self.subscriberCount) > int(other.subscriberCount)

    def __ge__(self, other):
        return int(self.subscriberCount) >= int(other.subscriberCount)

    def __lt__(self, other):
        return int(self.subscriberCount) < int(other.subscriberCount)

    def __le__(self, other):
        return int(self.subscriberCount) <= int(other.subscriberCount)


    @classmethod
    def get_service(cls):
        api_key = os.getenv('API_YUTUBE_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, filename):
        data = {
                'channel_id': self.__channel_id,
                'title': self.title,
                'description': self.description,
                'subscriberCount': self.subscriberCount,
                'url': self.url,
                'videoCount': self.video_count,
                'viewCount': self.viewCount
            }
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        intro = channel["items"][0]
        print(f'\nНазвание канала - {intro["snippet"]["title"]}')
        print(f'Описание канала - {intro["snippet"]["description"]}')
        print(f'Дата публикации канала - {intro["snippet"]["publishedAt"][:10]}')
        print(f'Количество просмотров - {intro["statistics"]["viewCount"]}  человек')
        print(f'Количество подписок - {intro["statistics"]["subscriberCount"]}  человек')
        print(f'Количество роликов на канале - {intro["statistics"]["videoCount"]}  человек')



