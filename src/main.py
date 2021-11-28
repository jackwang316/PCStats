import sys_gui
import cpu_gui
import mem_gui
import net_gui
from tkinter import *


def main():
    root = Tk()
    root.title("PC Statistics")
    root.configure(background="white")

    sys_gui.SysGui(root)
    mem_gui.MemGUI(root)
    cpu_gui.CPUGui(root)
    net_gui.NetGui(root)
    root.mainloop()


main()
