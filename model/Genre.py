import database.database as db
import datetime
from typing import Dict, List, NamedTuple

"""Информация о жанре"""


class Genre(NamedTuple):
    id: id
    name_rus: str
    name_eng: str
