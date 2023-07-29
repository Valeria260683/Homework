from random import randint
from Base import House, Consumer
from annotations import HouseAnnotation


NAMES = ["Alex", "John", "Peter", "Victor", "James", "Oliver"]
NAMES_COUNT = len(NAMES)


def generate_consumer():
    consumer = Consumer(
        name=NAMES[randint(0, NAMES_COUNT - 1)],
        account=randint(10_000, 250_000))
    return consumer


def generate_house_list(count: int) -> list[HouseAnnotation]:
    house_list = [House(
        price=randint(10_000, 250_000),
        square=randint(40, 150))for _ in range(count)]
    return house_list