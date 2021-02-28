import database.database as db
import datetime
from typing import Dict, List, NamedTuple
import common

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
        """Возвращает пользователя"""
        finded = None
        for user in self._users:
            if user.id == user_id:
                finded = user
        return finded  #

    @staticmethod
    def get_user_by_phone(self, phone: str) -> User:
        """Поиск пользователя по номеру телефона"""
        finded = None
        for user in self._users:
            if user.phone == phone:
                finded = user
        return finded

    def _get_all_users(self) -> List[tuple]:
        return self._users

    @staticmethod
    def add_user(name: str, phone: str) -> User:
        """Добавление нового пользователя и обновление информации о датах"""
        user = UserStore.get_user_by_phone(phone)
        if user is not None:
            db.update("user", {
                "id": user.id,
                "name": name,
                "phone": phone,
                "registered": user.registered,
                "last_visit": common.get_now_formatted()
            })
        else:
            db.insert("user", {
                "id": phone,
                "name": name,
                "phone": phone,
                "registered": common.get_now_formatted(),
                "last_visit": common.get_now_formatted()
            })
        return UserStore.get_user_by_phone(phone)
