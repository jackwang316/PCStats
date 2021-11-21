import psutil


def get_total_mem():
    return psutil.virtual_memory().total


def get_available_mem():
    return psutil.virtual_memory().available


def get_used_mem():
    return psutil.virtual_memory().used


def get_mem_used_percentage():
    return round((get_used_mem() / get_total_mem()) * 100, 2)


def get_mem_free():
    return psutil.virtual_memory().free


print(get_total_mem())
