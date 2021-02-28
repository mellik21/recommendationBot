import database.database as db
import datetime
from typing import List, NamedTuple

"""Информация о рекомендации"""

recommendation_columns = "id user_id anime_id score".split()


class Recommendation(NamedTuple):
    id: id
    user_id: int  # Many-to-one with user
    anime_id: int  # Many-to-one with anime
    score: float  # предположительные значения: -1, 0, 1


class RecommendationStore:
    def __init__(self):
        self._recommendations = self._load_recommendations()

    @staticmethod
    def _load_recommendations() -> List[Recommendation]:
        rows = db.fetchall("recommendation", recommendation_columns)
        recommendations = []
        for index, recommendation in enumerate(rows):
            recommendations.append(Recommendation(
                id=recommendation['id'],
                user_id=recommendation['user_id'],
                anime_id=recommendation['anime_id'],
                score=recommendation['score']
            ))
        return recommendations

    @staticmethod
    def add_assessment(user_id: int, anime_id: int, score: int):
        """Добавление нового пользователя и обновление информации о датах"""
        db.insert("assessment", {
            #  "id": phone,
            "user_id": user_id,
            "anime_id": anime_id,
            "score": score
        })

# TODO add get recommendation for user methods
