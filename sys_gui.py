from tkinter import *

import cpu_gui
import sys_info
import mem_gui

root = Tk()
root.title("PC Statistics")
root.geometry("640x720")
root.configure(background="white")

LABEL_PAD_X_WEST = (4, 10)
LABEL_PAD_Y = (0, 2)
LABEL_PAD_X_EAST = (220, 4)


class SysGui:

    sys_frame = None

    @classmethod
    def __init__(self, master):
        self.sys_frame = LabelFrame(master, width=600, height=120, background="white", fg="DodgerBlue3",
                                    text="System Information", font="Arial 20")
        self.sys_frame.pack(side=TOP)

        sys_title = Label(self.sys_frame, background="white", fg="black", text="Operating System: ", font="Arial 12")
        sys_title.grid(sticky="w", column=0, row=0, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_WEST)

        sys_label = Label(self.sys_frame, background="white", fg="dark turquoise", text=sys_info.get_system(),
                          font="Arial 12", anchor="e")
        sys_label.grid(sticky="E", column=1, row=0, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        pc_name_title = Label(self.sys_frame, background="white", fg="black", text="Desktop Name: ",
                              font="Arial 12", anchor="w")
        pc_name_title.grid(sticky="w", column=0, row=1, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_WEST)

        pc_name_label = Label(self.sys_frame, background="white", fg="dark turquoise", text=sys_info.get_pc_name(),
                              font="Arial 12", anchor="e")
        pc_name_label.grid(sticky="E", column=1, row=1, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        start_time_title = Label(self.sys_frame, background="white", fg="black", text="Boot Time: ",
                                 font="Arial 12", anchor="w")
        start_time_title.grid(sticky="w", column=0, row=2, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_WEST)

        start_time_label = Label(self.sys_frame, background="white", fg="dark turquoise",
                                 text=sys_info.get_startup_time(), font="Arial 12", anchor="e")
        start_time_label.grid(sticky="E", column=1, row=2, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        super_usr_title = Label(self.sys_frame, background="white", fg="black", text="Administrator: ",
                                font="Arial 12", anchor="w")
        super_usr_title.grid(sticky="w", column=0, row=3, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_WEST)

        super_usr_label = Label(self.sys_frame, background="white", fg="dark turquoise", text=sys_info.get_super_usr(),
                                font="Arial 12", anchor="e")
        super_usr_label.grid(sticky="E", column=1, row=3, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        battery_title = Label(self.sys_frame, background="white", fg="black", text="Battery: ",
                              font="Arial 12", anchor="w")
        battery_title.grid(sticky="w", column=0, row=4, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_WEST)

        battery_label = Label(self.sys_frame, background="white", fg="black", text=sys_info.get_battery(),
                              font="Arial 12", anchor="e")
        battery_label.grid(sticky="e", column=1, row=4, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)


SysGui(root)
mem_gui.MemGUI(root)
cpu_gui.CPUGui(root)
root.mainloop()
