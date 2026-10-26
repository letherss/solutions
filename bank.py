
class Account:
    def __init__(self, number, owner, balance=0):
        self.number = number
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount

    def __repr__(self):
        return (
            f"Account({self.number!r}, {self.owner!r}, "
            f"{self.balance!r})"
        )


class SavingsAccount(Account):
    def __init__(self, number, owner, balance=0, rate=0.05):
        super().__init__(number, owner, balance)
        self.rate = rate

    def add_interest(self):
        self._balance += self.balance * self.rate

    def __repr__(self):
        return (
            f"SavingsAccount({self.number!r}, {self.owner!r}, "
            f"{self.balance!r}, {self.rate!r})"
        )


class CheckingAccount(Account):
    def __init__(self, number, owner, balance=0, overdraft=0):
        super().__init__(number, owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if self.balance - amount < -self.overdraft:
            raise ValueError("Превышен лимит овердрафта")
        self._balance -= amount

    def __repr__(self):
        return (
            f"CheckingAccount({self.number!r}, {self.owner!r}, "
            f"{self.balance!r}, {self.overdraft!r})"
        )


if __name__ == "__main__":
    s = SavingsAccount("1", "Иван", 1000, rate=0.1)
    s.add_interest()
    s.balance

    try:
        s.withdraw(2000)
    except ValueError:
        pass

    try:
        s.balance = 0
    except AttributeError:
        pass

    c = CheckingAccount("2", "Мария", 100, overdraft=500)
    c.withdraw(400)
    c.balance

    try:
        c.withdraw(300)
    except ValueError:
        pass

    c.deposit(1000)
    c.balance
    isinstance(c, Account)
