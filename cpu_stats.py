import psutil
from win32com.client import GetObject


def get_processor():
    root_winmgmts = GetObject("winmgmts:root\cimv2")
    cpus = root_winmgmts.ExecQuery("Select * from Win32_Processor")
    return cpus[0].Name


def get_total_cpu_usage():
    return psutil.cpu_percent(interval=0.2)


def get_total_cpu_freq():
    return {psutil.cpu_freq(percpu=False).current}


def get_cpu_count():
    return psutil.cpu_count(logical=True)
