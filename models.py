from typing import Dict, List, NamedTuple

anime_name_columns = "id name".split()
anime_genre_columns = "id name_rus name_eng".split()
anime_columns = "id, page, name_rus, name_eng,  description, " \
                "alt_description, rating, picture_path, release_year,  " \
                "year_season, season, seria"
genre_columns = "id name_rus name_eng".split()

"""Информация об аниме"""


class Anime(NamedTuple):
    id: id
    page: int
    name_rus: str
    name_eng: str
    description: str
    alt_description: str
    studio: List[str]
    rating: float
    picture_path: str
    release_year: int
    year_season: str
    season: str
    seria: str
    genres: List[str]
    minor_names: List[str]

"""Информация о жанре"""


class Genre(NamedTuple):
    id: id
    name_rus: str
    name_eng: str


class User(NamedTuple):
    id: id
    phone: str
    name: str
    registered: str
    last_visit: str


class Studio(NamedTuple):
    id: id
    name: str
