import psutil
import converter


def get_total_mem():
    return converter.convert_from_byte(psutil.virtual_memory().total)


def get_available_mem():
    return converter.convert_from_byte(psutil.virtual_memory().available)


def get_used_mem():
    return converter.convert_from_byte(psutil.virtual_memory().used)


def get_mem_used_percentage():
    return str(round((psutil.virtual_memory().used / psutil.virtual_memory().total) * 100, 2)) + "%"


def get_mem_free():
    return converter.convert_from_byte(psutil.virtual_memory().free)


def get_swap_total():
    return converter.convert_from_byte(psutil.swap_memory().total)


def get_swap_used():
    return converter.convert_from_byte(psutil.swap_memory().used)


def get_swap_free():
    return converter.convert_from_byte(psutil.swap_memory().free)


def get_swap_used_percent():
    return str(round((psutil.swap_memory().used / psutil.swap_memory().total) * 100, 2)) + "%"
