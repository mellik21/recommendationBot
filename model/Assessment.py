import database.database as db
from typing import List, NamedTuple

"""Информация о пользовательской оценке"""

assessment_columns = "id user_id anime_id score".split()


class Assessment(NamedTuple):
    id: id
    user_id: int  # Many-to-one with user
    anime_id: int  # Many-to-one with anime
    score: int  # предположительные значения: -1, 0, 1


class AssessmentStore:
    def __init__(self):
        self._assessments = self._load_assessments()

    @staticmethod
    def _load_assessments() -> List[Assessment]:
        rows = db.fetchall("assessment", assessment_columns)
        assessments = []
        for index, assessment in enumerate(rows):
            assessments.append(Assessment(
                id=assessment['id'],
                user_id=assessment['user_id'],
                anime_id=assessment['anime_id'],
                score=assessment['score']
            ))
        return assessments

    @staticmethod
    def add_assessment(user_id: int, anime_id: int, score: int):
        """Добавление нового пользователя и обновление информации о датах"""
        db.insert("assessment", {
            #  "id": phone,
            "user_id": user_id,
            "anime_id": anime_id,
            "score": score
        })

