import database.database as db
import datetime
from typing import List, NamedTuple

"""Информация о пользовательской оценке"""


class Assessment(NamedTuple):
    id: id
    user_id: int  # Many-to-one with user
    anime_id: int  # Many-to-one with anime
    score: int  # предположительные значения: -1, 0, 1
