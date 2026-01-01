class PiggyBank:
    def __init__(self):
        self.balance = 0

    def add_money(self, amount: int):
        self.balance += amount

    def take_money(self, amount: int):
        if amount <= self.balance:
            self.balance -= amount

    def get_balance(self) -> int:
        return self.balance

bank = PiggyBank()
bank.add_money(220)
bank.add_money(200)
bank.take_money(400)
print(bank.get_balance())


class Bank:
    def __init__(self):
        self.money = 0

    def add_money(self, amount: int):
        self.money += amount

    def take_money(self, amount: int):
        if amount <= self.money:
            self.money -= amount
        else:
            raise AssertionError("Ошибка")

    def get_balance(self) -> int:
        return self.money

hhh = Bank()
hhh.add_money(200)
hhh.add_money(300)
hhh.take_money(400)
print(hhh.get_balance())
