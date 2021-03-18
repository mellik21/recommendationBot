import database.db_helper as db
import datetime
from typing import Dict, List, NamedTuple

"""Информация о жанре"""

genre_columns = "id name_rus name_eng".split()


class Genre(NamedTuple):
    id: id
    name_rus: str
    name_eng: str


class GenreStore:
    def __init__(self):
        self._genres = self._load_genres()

    @staticmethod
    def _load_genres() -> List[Genre]:
        rows = db.fetchall("genre", genre_columns)
        genres = []
        for index, anime in enumerate(rows):
            genres.append(Genre(
                id=anime['id'],
                name_rus=anime['name_rus'],
                name_eng=anime['name_eng'],
            ))
        return genres

    def get_genre_by_id(self, genre_id: str) -> Genre:
        finded = None
        for anime in self._genres:
            if anime.id == genre_id:
                finded = anime
        return finded
