def guests_by_seat(seats):
    result = [0] * len(seats)
    for guest in range(len(seats)):
        seat = seats[guest]
        result[seat - 1] = guest + 1
    return result

if __name__ == "__main__":
    print(guests_by_seat([1, 2, 3, 5, 4]))
    print(guests_by_seat([11, 6, 8, 2, 10, 9, 4, 7, 3, 1, 5]))

