def min_pair_sum(numbers):
    numbers = sorted(numbers)
    total = 0

    for i in range(len(numbers) // 2):
        total += numbers[i] * numbers[-(i + 1)]

    return total

if __name__ == "__main__":
    print(min_pair_sum([5, 4, 2, 3]))
    print(min_pair_sum([12, 6, 10, 26, 3, 24]))

    