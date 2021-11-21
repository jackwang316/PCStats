import platform
from datetime import datetime
import psutil

uname = platform.uname()


def get_system():
    return uname.system + " " + get_version()


def get_pc_name():
    return uname.node


def get_version():
    return uname.version


def get_startup_time():
    return datetime.fromtimestamp(psutil.boot_time())
