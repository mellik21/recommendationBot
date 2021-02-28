import database.database as db
import datetime
from typing import List, NamedTuple

"""Информация о рекомендации"""


class Recommendation(NamedTuple):
    id: id
    user_id: int  # Many-to-one with user
    anime_id: int  # Many-to-one with anime
    score: float  # предположительные значения: -1, 0, 1
