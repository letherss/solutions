def index_of_min(values):
    if len(values) == 0:
        return -1

    min_value = values[0]
    min_index = 0

    for i in range(len(values)):
        if values[i] < min_value:
            min_value = values[i]
            min_index = i

    return min_index

print(index_of_min([10, -3, -5, 2, 5]))
print(index_of_min([1, 2, 3]))
print(index_of_min([4, 1, 1, 9]))
print(index_of_min([]))