def is_disarium(n):
    total = 0
    for i, digit in enumerate(str(n), start=1):
        total += int(digit) ** i
    return total == n

print(is_disarium(89))
print(is_disarium(135))
print(is_disarium(564))