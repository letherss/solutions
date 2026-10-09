def is_automorphic(n):
    square = n * n
    digits = len(str(n))
    return square % (10 ** digits) == n

if __name__ == "__main__":
    (is_automorphic(25))
    (is_automorphic(76))
    (is_automorphic(5))
    (is_automorphic(13))