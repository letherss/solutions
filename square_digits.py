def square_digits(n):
    result = ""
    for digit in str(n):
        result += str(int(digit) ** 2)
    return int(result)

if __name__ == "__main__":
    (square_digits(3212))
    (square_digits(2112))
    (square_digits(0))
    (square_digits(999))
    (square_digits(10001))

