import database.database as db
import datetime
from typing import List, NamedTuple
import model.Genre as Genre

"""Информация об аниме"""


class Anime(NamedTuple):
    id: id
    name_rus: str
    name_eng: str
    release_date: datetime.datetime
    description: str
    alternative_description: str
    studio: str
    episodes_number: int
    episodes_duration: int
    score: float
    picture_path: str
    genres: List[Genre]  # Many-to-many anime_genres
    names: List[str]  # One-to-many anime_names
