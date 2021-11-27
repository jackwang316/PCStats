from tkinter import *
import mem_info

LABEL_PAD_X_WEST = (4, 10)
LABEL_PAD_X_EAST = (10, 10)
LABEL_PAD_Y = (0, 2)
LABEL_HEIGHT = 1
LABEL_WIDTH = 6


class MemGUI:
    mem_frame = None
    master = None

    available_mem_val = None
    used_mem_val = None
    used_mem_percent_val = None
    free_mem_val = None

    swap_used_val = None
    swap_free_val = None
    swap_used_percent = None

    def __init__(self, master):
        self.master = master
        self.init_frame()
        self.init_titles()
        self.init_mem_vals()
        self.init_swap_vals()
        self.updater()

    def init_frame(self):
        self.mem_frame = LabelFrame(self.master, width=595, height=150, background="white", fg="DodgerBlue3",
                                    text="Memory Information", font="Arial 20")
        self.mem_frame.pack(side=TOP, pady=LABEL_PAD_X_EAST)
        self.mem_frame.grid_propagate(0)

    def init_titles(self):
        phys_mem_title = Label(self.mem_frame, background="white", fg="black", text="Physical Memory: ",
                               font="Arial 12", anchor="w")
        phys_mem_title.grid(sticky="w", column=0, row=1, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_WEST)

        swap_mem_title = Label(self.mem_frame, background="white", fg="black", text="Swap Memory: ",
                               font="Arial 12", anchor="w")
        swap_mem_title.grid(sticky="w", column=0, row=2, pady=(10, 2), padx=LABEL_PAD_X_WEST)

        total_title = Label(self.mem_frame, background="white", fg="black", text="Total", font="Arial 12 bold")
        total_title.grid(sticky="n", column=1, row=0, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        available_title = Label(self.mem_frame, background="white", fg="black", text="Available", font="Arial 12 bold")
        available_title.grid(sticky="n", column=2, row=0, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        used_title = Label(self.mem_frame, background="white", fg="black", text="Used", font="Arial 12 bold")
        used_title.grid(sticky="n", column=3, row=0, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        free_title = Label(self.mem_frame, background="white", fg="black", text="Free", font="Arial 12 bold")
        free_title.grid(sticky="n", column=4, row=0, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        percent_title = Label(self.mem_frame, background="white", fg="black", text="Percent", font="Arial 12 bold")
        percent_title.grid(sticky="n", column=5, row=0, pady=LABEL_PAD_Y, padx=(10, 0))

    def init_mem_vals(self):
        total_mem_val = Label(self.mem_frame, fg="DodgerBlue3", height=LABEL_HEIGHT, width=LABEL_WIDTH,
                              text=mem_info.get_total_mem(), font="Arial 11")
        total_mem_val.grid(sticky="n", column=1, row=1, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        self.available_mem_val = Label(self.mem_frame, fg="DodgerBlue3", height=LABEL_HEIGHT, width=LABEL_WIDTH,
                                       text=mem_info.get_available_mem(), font="Arial 11")
        self.available_mem_val.grid(sticky="n", column=2, row=1, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        self.used_mem_val = Label(self.mem_frame, fg="DodgerBlue3", height=LABEL_HEIGHT, width=LABEL_WIDTH,
                                  text=mem_info.get_used_mem(), font="Arial 11")
        self.used_mem_val.grid(sticky="n", column=3, row=1, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        self.free_mem_val = Label(self.mem_frame, fg="DodgerBlue3", height=LABEL_HEIGHT, width=LABEL_WIDTH,
                                  text=mem_info.get_mem_free(), font="Arial 11")
        self.free_mem_val.grid(sticky="n", column=4, row=1, pady=LABEL_PAD_Y, padx=LABEL_PAD_X_EAST)

        self.used_mem_percent_val = Label(self.mem_frame, fg="DodgerBlue3", height=LABEL_HEIGHT, width=LABEL_WIDTH,
                                          text=mem_info.get_mem_used_percentage(), font="Arial 11")
        self.used_mem_percent_val.grid(sticky="n", column=5, row=1, pady=LABEL_PAD_Y, padx=(10, 0))

    def init_swap_vals(self):
        total_swap_val = Label(self.mem_frame, fg="DodgerBlue3", height=LABEL_HEIGHT, width=LABEL_WIDTH,
                               text=mem_info.get_swap_total(), font="Arial 11")
        total_swap_val.grid(sticky="n", column=1, row=2, pady=(10, 2), padx=LABEL_PAD_X_EAST)

        available_swap_val = Label(self.mem_frame, fg="DodgerBlue3", height=LABEL_HEIGHT, width=LABEL_WIDTH,
                                   text="NONE", font="Arial 11")
        available_swap_val.grid(sticky="n", column=2, row=2, pady=(10, 2), padx=LABEL_PAD_X_EAST)

        self.swap_used_val = Label(self.mem_frame, fg="DodgerBlue3", height=LABEL_HEIGHT, width=LABEL_WIDTH,
                                   text=mem_info.get_swap_used(), font="Arial 11")
        self.swap_used_val.grid(sticky="n", column=3, row=2, pady=(10, 2), padx=LABEL_PAD_X_EAST)

        self.swap_free_val = Label(self.mem_frame, fg="DodgerBlue3", height=LABEL_HEIGHT, width=LABEL_WIDTH,
                                   text=mem_info.get_swap_free(), font="Arial 11")
        self.swap_free_val.grid(sticky="n", column=4, row=2, pady=(10, 2), padx=LABEL_PAD_X_EAST)

        self.swap_used_percent = Label(self.mem_frame, fg="DodgerBlue3", height=LABEL_HEIGHT, width=LABEL_WIDTH,
                                       text=mem_info.get_swap_used_percent(), font="Arial 11")
        self.swap_used_percent.grid(sticky="n", column=5, row=2, pady=(10, 2), padx=(10, 0))

    def update_avail_mem(self):
        self.available_mem_val.configure(text=mem_info.get_available_mem())

    def update_used_mem(self):
        self.used_mem_val.configure(text=mem_info.get_used_mem())

    def update_free_mem(self):
        self.free_mem_val.configure(text=mem_info.get_mem_free())

    def update_used_percentage(self):
        self.used_mem_percent_val.configure(text=mem_info.get_mem_used_percentage())

    def update_swap_used(self):
        self.swap_used_val.configure(text=mem_info.get_swap_used())

    def update_swap_free(self):
        self.swap_free_val.configure(text=mem_info.get_swap_free())

    def update_swap_percentage(self):
        self.swap_used_percent.configure(text=mem_info.get_swap_used_percent())

    def updater(self):
        self.update_avail_mem()
        self.update_used_mem()
        self.update_free_mem()
        self.update_used_percentage()
        self.update_swap_used()
        self.update_swap_free()
        self.update_swap_percentage()
        self.master.after(1000, self.updater)
