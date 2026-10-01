def circle_diameter(radius):
    return radius * 2


def sum_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total = total + i
    return total

if __name__ == "__main__":
    print(circle_diameter(5))
    print(sum_range(100, 500))
    print(sum_range(1, 10))
    print(sum_range(500, 500))
