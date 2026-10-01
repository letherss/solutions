def bytes_to_kilobytes(kilobytes):
    bytes = kilobytes / 1024
    return bytes


def kilobytes_to_bytes(bytes):
    kilobytes = bytes * 1024
    return kilobytes


if __name__ == "__main__":
    print(bytes_to_kilobytes(2048))
    print(kilobytes_to_bytes(2))

