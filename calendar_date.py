
class Date:
    def __init__(self, day, month, year):
        if year < 1 or month < 1 or month > 12:
            raise ValueError

        if day < 1 or day > self.days_in_month(month, year):
            raise ValueError

        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_leap(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    @staticmethod
    def days_in_month(month, year):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and Date.is_leap(year):
            return 29
        return days[month - 1]

    def to_number(self):
        y = self.year - 1
        total = 365 * y + y // 4 - y // 100 + y // 400

        for m in range(1, self.month):
            total += self.days_in_month(m, self.year)

        return total + self.day - 1

    @classmethod
    def from_number(cls, number):
        if number < 0:
            raise ValueError

        left, right = 1, number // 365 + 2

        while left < right:
            mid = (left + right + 1) // 2
            y = mid - 1
            days = 365 * y + y // 4 - y // 100 + y // 400

            if days <= number:
                left = mid
            else:
                right = mid - 1

        year = left
        remaining = number - (
            365 * (year - 1) + (year - 1) // 4
            - (year - 1) // 100 + (year - 1) // 400
        )

        month = 1
        while remaining >= cls.days_in_month(month, year):
            remaining -= cls.days_in_month(month, year)
            month += 1

        return cls(remaining + 1, month, year)

    def __add__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        return Date.from_number(self.to_number() + n)

    def __sub__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return self.to_number() - other.to_number()

    def __eq__(self, other):
        return isinstance(other, Date) and self.to_number() == other.to_number()

    def __lt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return self.to_number() < other.to_number()

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year:04d}"

if __name__ == "__main__":
    d = Date(31, 12, 2025)

    print(d + 1)
    print(d + 60)
    print(Date(1, 3, 2024) + (-1))
    print(Date(1, 1, 2026) - Date(1, 1, 2025))
    print(str(Date(9, 5, 1945)))
    print(repr(Date(1, 1, 2026)))
    print(Date(1, 1, 2025) < Date(1, 1, 2026))
    print(Date(1, 1, 2026) == Date(1, 1, 2026))
    print(d + 1_000_000)

    try:
        Date(29, 2, 2025)
    except ValueError:
        print("ValueError")