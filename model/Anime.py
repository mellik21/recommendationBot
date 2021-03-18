import database.db_helper as db
import datetime
from typing import List, NamedTuple
from model import Genre
from model.Genre import GenreStore

"""Информация об аниме"""
anime_name_columns = "id name".split()
anime_genre_columns = "id name_rus name_eng".split()
anime_columns = "id name_rus name_eng release_date description alternative_description studio episodes_number " \
                "episodes_duration score picture_path".split()


class Anime(NamedTuple):
    id: id
    name_rus: str
    name_eng: str
    release_date: datetime.datetime
    description: str
    alternative_description: str
    studio: str
    #  episodes_number: int
    #  episodes_duration: int
    rating: float
    picture_path: str
    genres: List[Genre]  # Many-to-many anime_genres
    minor_names: List[str]  # One-to-many anime_names


class AnimeStore:
    def __init__(self):
        self._animes = self._load_animes()

    @staticmethod
    def _load_animes() -> List[Anime]:
        anime_rows = db.fetchall("anime", anime_columns)
        animes = []
        for index, anime in enumerate(anime_rows):
            animes.append(Anime(
                id=anime['id'],
                name_rus=anime['name_rus'],
                name_eng=anime['name_eng'],
                release_date=anime['release_date'],
                description=anime['description'],
                alternative_description=anime['alternative_description'],
                studio=anime['studio'],
                episodes_number=anime['episodes_number'],
                episodes_duration=anime['episodes_duration'],
                score=anime['score'],
                picture_path=anime['picture_path'],
                genres=AnimeStore.get_anime_genres(anime['id']),
                names=AnimeStore.get_anime_names(anime['id'])
            ))
        return animes

    @staticmethod
    def get_anime_genres(anime_id: int) -> List[Genre]:
        """Возвращает список жанров"""
        genres = []
        genres_rows = db.select_by_column("anime_genre", "anime_genre".split(), "anime_id", anime_id)
        for index, genre in enumerate(genres_rows):
            genres.append(GenreStore().get_genre_by_id(genre['id']))
        return genres

    @staticmethod
    def get_anime_names(anime_id: int) -> List[str]:
        """Возвращает список альтернативных названий"""
        names = []
        names_rows = db.select_by_column("anime_name", anime_name_columns, "anime_id", anime_id)
        for name in enumerate(names_rows):
            names.append(name['name'])
        return names

# adding anime not included
