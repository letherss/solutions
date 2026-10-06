def sum_interval(a, b):
    start = min(a, b)
    end = max(a, b)
    n = end - start + 1
    return n * (start + end) // 2

if __name__ == "__main__":
    print(sum_interval(1, 0))
    print(sum_interval(1, 2))
    print(sum_interval(-1, 2))
    print(sum_interval(5, 5))

