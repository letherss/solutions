def truth_table(n):
    result = []
    for i in range(2 ** n):
        row = []
        for j in range(n - 1, -1, -1):
            row.append((i >> j) & 1)
        result.append(tuple(row))
    return result

if __name__ == "__main__":
    (truth_table(1))
    (truth_table(2))
    (truth_table(3))
    (truth_table(0))