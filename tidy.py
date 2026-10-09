def is_tidy(n):
    digits = str(n)
    return digits == "".join(sorted(digits))

if __name__ == "__main__":
    (is_tidy(12))
    (is_tidy(32))
    (is_tidy(13579))
    (is_tidy(2335))
    (is_tidy(7))