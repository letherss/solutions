def shortest_distance(kilometers, meters):
    kilometers_in_meters = kilometers * 1000
    if kilometers_in_meters < meters:
        return kilometers_in_meters
    else:
        return meters

if __name__ == "__main__":
    print(shortest_distance(1, 500))
    print(shortest_distance(0.2, 900))
    print(shortest_distance(1, 1000))