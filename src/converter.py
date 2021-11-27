import math

UNITS = ("B", "KB", "MB", "GB", "TB")


def convert_from_byte(byte_size):
    if byte_size == 0:
        return "0B"
    i = int(math.floor(math.log(byte_size, 1024)))
    p = math.pow(1024, i)
    s = round(byte_size / p, 2)
    return str(s) + UNITS[i]
