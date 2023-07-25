# 3. В файле main.py импортируем функцию `get_user_recommendations`
# из recommendations.py и создаем экземпляры класса User
# с аннотациями типов данных.


from recommendations import get_user_recommendations
from annotations import User

user1 = User(user_id=1, name="John")
user2 = User(user_id=2, name="Alice")

recommendations1 = get_user_recommendations(user1)
recommendations2 = get_user_recommendations(user2)

print(recommendations1)
print(recommendations2)