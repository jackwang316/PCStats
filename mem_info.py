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


def get_swap_total():
    return psutil.swap_memory().total


def get_swap_used():
    return psutil.swap_memory().used


def get_swap_free():
    return psutil.swap_memory().free


def get_swap_used_percent():
    return round((get_swap_used() / get_swap_total()) * 100, 2)


print(get_total_mem())
