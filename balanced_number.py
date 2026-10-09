def is_balanced_number(n):
    digits = str(n)
    length = len(digits)
    middle = length // 2
    if length % 2 == 0:
        left = digits[:middle - 1]
        right = digits[middle + 1:]
    else:
        left = digits[:middle]
        right = digits[middle + 1:]
    left_sum = sum(int(digit) for digit in left)
    right_sum = sum(int(digit) for digit in right)
    if left_sum == right_sum:
        return "Balanced"
    else:
        return "Not Balanced"

if __name__ == "__main__":
    (is_balanced_number(7))
    (is_balanced_number(59))
    (is_balanced_number(295591))
    (is_balanced_number(424))
    (is_balanced_number(13623))