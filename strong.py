import math
def is_strong(n):
    total = 0
    for digit in str(n):
        total += math.factorial(int(digit))
    return total == n

if __name__ == "__main__":
    (is_strong(1))
    (is_strong(2))
    (is_strong(145))
    (is_strong(123))

    strong_numbers = []
    for number in range(1, 100000):
        if is_strong(number):
            strong_numbers.append(number)
    (strong_numbers)