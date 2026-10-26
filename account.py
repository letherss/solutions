class  Account:
    def __init__(self, number, owner, balance):
        if balance < 0: raise ValueError("Счёт не может быть отрицательным")
        self.number = number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance - amount < 0: raise ValueError("недостаточно средств")
        self.balance -= amount
        return self.balance
    def __repr__(self, amount):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"
acc = Account(number="1", owner="Иван", balance=1000)

if __name__ == "__main__":
    (acc.deposit(500))
    (acc.balance)
    (acc.withdraw(200))
    (acc.balance)
    (acc.withdraw(5000))
    (acc.balance)
    (acc)