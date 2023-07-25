#2. В файле annotations.py создадим аннотации типов данных для функции
# `get_user_recommendations` и класса User.


from typing import List

class User:
  def __init__(self, user_id: int, name: str):
      self.user_id: int = user_id
      self.name: str = name

  def get_user_recommendations(user: "User") -> List[str]:
      recommendations: List[str] = []
      recommendations.append(f"Рекомендация 1 для пользователя {user.name}")
      recommendations.append(f"Рекомендация 2 для пользователя {user.name}")
      recommendations.append(f"Рекомендация 3 для пользователя {user.name}")
      return recommendations