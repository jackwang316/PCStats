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


def get_battery():
    return psutil.sensors_battery()


def get_super_usr():
    return psutil.users()[0].name
