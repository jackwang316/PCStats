import psutil
import converter


def get_bytes_sent():
    return converter.convert_from_byte(psutil.net_io_counters().bytes_sent)


def get_bytes_recv():
    return converter.convert_from_byte(psutil.net_io_counters().bytes_recv)


def get_packs_sent():
    return psutil.net_io_counters().packets_sent


def get_packs_recv():
    return psutil.net_io_counters().packets_recv


def get_errin():
    return psutil.net_io_counters().errin


def get_errout():
    return psutil.net_io_counters().errout


def get_drop_in():
    return psutil.net_io_counters().dropin


def get_drop_out():
    return psutil.net_io_counters().dropout
