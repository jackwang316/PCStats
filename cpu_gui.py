from tkinter import *
import cpu_stats


class CPUGui:
    cpu_frame = None
    master = None

    def __init__(self, master):
        self.master = master
        self.init_frame()
        self.init_titles()
        self.init_cpu_vals()

    def init_frame(self):
        self.cpu_frame = LabelFrame(self.master, width=600, height=120, background="white", fg="DodgerBlue3",
                                    text="CPU Information", font="Arial 20")
        self.cpu_frame.pack(side=TOP, pady=(10, 10))

    def init_titles(self):
        cpu_name_title = Label(self.cpu_frame, background="white", fg="black", text="Processor Name: ",
                               font="Arial 12", anchor="w")
        cpu_name_title.grid(sticky="W", column=0, row=0, pady=(0, 2), padx=(4, 10))

        cpu_usage_title = Label(self.cpu_frame, background="white", fg="black", text="Total Usage: ",
                                font="Arial 12", anchor="w")
        cpu_usage_title.grid(sticky="W", column=0, row=1, pady=(0, 2), padx=(4, 10))

        cpu_freq_title = Label(self.cpu_frame, background="white", fg="black", text="Max Frequency: ",
                               font="Arial 12", anchor="w")
        cpu_freq_title.grid(sticky="W", column=0, row=2, pady=(0, 2), padx=(4, 10))

        phys_core_title = Label(self.cpu_frame, background="white", fg="black", text="Physical Cores: ",
                                font="Arial 12", anchor="w")
        phys_core_title.grid(sticky="W", column=0, row=3, pady=(0, 2), padx=(4, 10))

        logic_core_title = Label(self.cpu_frame, background="white", fg="black", text="Logical Cores: ",
                                 font="Arial 12", anchor="w")
        logic_core_title.grid(sticky="W", column=0, row=4, pady=(0, 2), padx=(4, 10))

    def init_cpu_vals(self):
        cpu_name_label = Label(self.cpu_frame, background="white", fg="DodgerBlue3", text=cpu_stats.get_processor(),
                               font="Arial 12", anchor="e")
