def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def arrangements(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    result = 1
    for i in range(n - k + 1, n + 1):
        result *= i
    return result
def combinations(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result

if __name__ == "__main__":
    (factorial(0))
    (factorial(5))
    (factorial(-1))

    (arrangements(13, 6))
    (arrangements(4, 2))
    (arrangements(5, 5))
    (arrangements(3, 5))

    (combinations(13, 6))
    (combinations(4, 2))
    (combinations(64, 8))
    (combinations(5, 0))