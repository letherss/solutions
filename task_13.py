def multiplication_table(n):
    result = []
    for i in range(1, 11):
        result.append(f"{n} x {i} = {n * i}")
    return result

if __name__ == "__main__":
    print(multiplication_table(7))
