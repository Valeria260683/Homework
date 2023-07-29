__all__ = {"House", "Consumer"}
class House:
    def __init__(self, price: float, square: float):
        self.price = price
        self.square = square

    def __repr__(self):
        return f"{self.price}$ - {self.square}m"

    def __str__(self):
        return f"{self.price}$ - {self.square}m"


class Consumer:
    def __init__(self, name: str, account: float):
        self.name = name
        self.account = account

    def __repr__(self):
        return {"name": self.name, "account": self.account}

    def __str__(self):
        return f"{self.name} - {self.account}$"


