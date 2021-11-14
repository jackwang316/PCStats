import psutil
import wmi

def getTotalCPUsage():
    return psutil.cpu_percent(interval=0.2)

def getTotalCPUFreq():
    return {psutil.cpu_freq(percpu=False).current}

def getCPUCount():
    return psutil.cpu_count(logical=True)
