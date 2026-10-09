def pasture_area(wire, w):
    l = (wire - 2 * w) / 3
    return w * l
def best_pasture(wire):
    w = wire / 4
    l = wire / 6
    area = pasture_area(wire, w)
    return (w, l, area)

if __name__ == "__main__":
    (pasture_area(100, 25))
    (pasture_area(100, 10))
    (pasture_area(100, 50))
    (best_pasture(100))
    (best_pasture(60))
    (best_pasture(12))