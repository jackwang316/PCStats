from tkinter import *
import cpu_stats


class CPUGui:
    cpu_frame = None
    master = None
    cpu_usage_val = None

    def __init__(self, master):
        self.master = master
        self.init_frame()
        self.init_titles()
        self.init_cpu_vals()
        self.cpu_updater()

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
        cpu_name_val = Label(self.cpu_frame, background="white", fg="DodgerBlue3", text=cpu_stats.get_processor(),
                             font="Arial 12", anchor="e")
        cpu_name_val.grid(sticky="E", column=1, row=0, pady=(0, 2), padx=(174, 4))

        self.cpu_usage_val = Label(self.cpu_frame, background="white", fg="DodgerBlue3",
                                   text=str(cpu_stats.get_total_cpu_usage()) + "%", font="Arial 12", anchor="e")
        self.cpu_usage_val.grid(sticky="E", column=1, row=1, pady=(0, 2), padx=(174, 4))

        cpu_freq_val = Label(self.cpu_frame, background="white", fg="DodgerBlue3", text=cpu_stats.get_total_cpu_freq(),
                             font="Arial 12", anchor="e")
        cpu_freq_val.grid(sticky="E", column=1, row=2, pady=(0, 2), padx=(174, 4))

        cpu_phys_val = Label(self.cpu_frame, background="white", fg="DodgerBlue3", text=cpu_stats.get_phys_core_count(),
                             font="Arial 12", anchor="e")
        cpu_phys_val.grid(sticky="E", column=1, row=3, pady=(0, 2), padx=(174, 4))

        cpu_logic_val = Label(self.cpu_frame, background="white", fg="DodgerBlue3",
                              text=cpu_stats.get_logical_core_count(), font="Arial 12", anchor="e")
        cpu_logic_val.grid(sticky="E", column=1, row=4, pady=(0, 2), padx=(174, 4))

    def update_cpu_usage(self):
        self.cpu_usage_val.configure(text=str(cpu_stats.get_total_cpu_usage()) + "%")

    def cpu_updater(self):
        self.update_cpu_usage()
        self.master.after(4000, self.cpu_updater)
