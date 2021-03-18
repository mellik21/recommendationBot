import sqlalchemy as db
import database.repository as rep
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
    page: int
    name_rus: str
    name_eng: str
    description: str
    alt_description: str
    studio: str
    rating: float
    picture_path: str
    release_year: int
    year_season: str
    season: str
    seria: str
    genres: str
    minor_names: str

