def square_digits(n):
    result = ""
    for digit in str(n):
        result += str(int(digit) ** 2)
    return int(result)

print(square_digits(3212))
print(square_digits(2112))
print(square_digits(0))
print(square_digits(999))
print(square_digits(10001))

