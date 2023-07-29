from generators import generate_consumer, generate_house_list
from annotations import HouseAnnotation, ConsumerAnnotation

def get_recommendations(house_list: HouseAnnotation, consumer: ConsumerAnnotation) -> str:
    avaliable_houses = [house for house in house_list if house.price < consumer.account]

    if avaliable_houses.sort(key=lambda x: x.square):
        return f"Best variant for {consumer.name} is {avaliable_houses[-1]}"
    else:
        return "No houses founded"



consumer = generate_consumer()
house_list = generate_house_list(count=5)
print(consumer)
print(house_list)