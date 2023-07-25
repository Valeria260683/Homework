"""Решить задачу на создание списка рекомендаций,
сделать аннотации типов данных в функциональном программировании
и сделать аннотации для экземпляров классов."""

# 1. В файле recommendations.py создадим функцию `get_user_recommendations`,
# которая будет принимать на вход пользователя и возвращать список
# рекомендаций для этого пользователя.


from typing import List

class User:
    def __init__(self, user_id: int, name: str):
        self.user_id: int = user_id
        self.name: str = name

def get_user_recommendations(user: User) -> List[str]:
    recommendations = []
    recommendations.append(f"Рекомендация 1 для пользователя {user.name}")
    recommendations.append(f"Рекомендация 2 для пользователя {user.name}")
    recommendations.append(f"Рекомендация 3 для пользователя {user.name}")
    return recommendations