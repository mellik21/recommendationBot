import database.database as db
import datetime
from typing import Dict, List, NamedTuple

"""Информация о пользователе"""


class User(NamedTuple):
    id: id
    name: str
    phone: int
    registered: datetime.datetime
    last_visit: datetime.datetime


class UserStore:
    def __init__(self):
        self._users = self._load_users()

    @staticmethod
    def _load_users() -> List[User]:
        rows = db.fetchall("user", "id name phone registered last_visit".split())
        users = []
        for index, user in enumerate(rows):
            users.append(User(
                id=user['id'],
                name=user['name'],
                phone=user['phone'],
                registered=user['registered'],
                last_visit=user['last_visit']
            ))
        return users

    def _get_user_by_id(self, user_id: str) -> User:
        finded = None
        for user in self._users:
            if user.id == user_id:
                finded = user
        return finded  #

    def _get_user_by_phone(self, phone: str) -> User:
        finded = None
        for user in self._users:
            if user.phone == phone:
                finded = user
        return finded

    def _get_all_users(self) -> List[tuple]:
        return self._users

    @staticmethod
    def add_user(name: str, phone: str) -> User:

        user = UserStore._get_user_by_phone(phone)
        if user is not None:
            db.insert("user", {
                "time_count": parsed_message.time_count,
                "created": _get_now_formatted(),
                "category_codename": category.codename,
                "raw_text": raw_message
            })
        else:
            db.insert("user", {
                "time_count": parsed_message.time_count,
                "created": _get_now_formatted(),
                "category_codename": category.codename,
                "raw_text": raw_message
            })

        return User(id=None,
                    category_codename=category.codename)
