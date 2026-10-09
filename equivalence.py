def are_equivalent(f, g, n):
    for row in truth_table(n):
        if f(*row) != g(*row):
            return False
    return True

def truth_table(n):
    result = []
    for i in range(2 ** n):
        row = []
        for j in range(n - 1, -1, -1):
            row.append((i >> j) & 1)
        result.append(tuple(row))
    return result

def wrong(a, b):
    return (not a) and (not b)
def de_morgan_left(a, b):
    return not (a and b)
def de_morgan_right(a, b):
    return (not a) or (not b)
def de_morgan_second_left(a, b):
    return not (a or b)
def de_morgan_second_right(a, b):
    return (not a) and (not b)
def implies(a, b):
    return (not a) or b
def implication_left(a, b):
    return implies(a, b)
def implication_right(a, b):
    return (not a) or b
def contraposition_left(a, b):
    return implies(a, b)
def contraposition_right(a, b):
    return implies(not b, not a)
def distributive_left(a, b, c):
    return a and (b or c)
def distributive_right(a, b, c):
    return (a and b) or (a and c)

if __name__ == "__main__":
    (are_equivalent(de_morgan_left, de_morgan_right, 2))
    (are_equivalent(de_morgan_left, wrong, 2))
    (are_equivalent(de_morgan_second_left, de_morgan_second_right, 2))
    (are_equivalent(implication_left, implication_right, 2))
    (are_equivalent(contraposition_left, contraposition_right, 2))
    (are_equivalent(distributive_left, distributive_right, 3))