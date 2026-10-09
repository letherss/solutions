def is_disarium(n):
    total = 0
    for i, digit in enumerate(str(n), start=1):
        total += int(digit) ** i
    return total == n

if __name__ == "__main__":
    (is_disarium(89))
    (is_disarium(135))
    (is_disarium(564))