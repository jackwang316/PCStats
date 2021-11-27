from tkinter import *
import net_info


class NetGui:
    net_frame = None
    net_err_frame = None
    master = None

    bytes_sent_val = None
    bytes_recv_val = None
    packs_sent_val = None
    packs_recv_val = None

    errin_val = None
    errout_val = None
    dropin_val = None
    dropout_val = None

    def __init__(self, master):
        self.master = master
        self.init_frame()
        self.init_net_titles()
        self.init_net_err_titles()
        self.init_net_vals()
        self.init_net_err_vals()
        self.net_updater()

    def init_frame(self):
        self.net_frame = LabelFrame(self.master, width=285, height=150, background="white", fg="DodgerBlue3",
                                    text="Network I/O", font="Arial 20")
        self.net_frame.pack(side=LEFT, anchor="n", pady=(10, 10), padx=(20, 0))
        self.net_frame.grid_propagate(0)

        self.net_err_frame = LabelFrame(self.master, width=285, height=150, background="white", fg="DodgerBlue3",
                                        text="Network Error", font="Arial 20")
        self.net_err_frame.pack(side=TOP, anchor="e", pady=(10, 10), padx=(0, 20))
        self.net_err_frame.grid_propagate(0)

    def init_net_titles(self):
        bytes_sent_title = Label(self.net_frame, background="white", fg="black", text="Bytes sent: ",
                                 font="Arial 12", anchor="w")
        bytes_sent_title.grid(sticky="w", column=0, row=0, pady=(0, 2), padx=(4, 10))

        bytes_recv_title = Label(self.net_frame, background="white", fg="black", text="Bytes received: ",
                                 font="Arial 12", anchor="w")
        bytes_recv_title.grid(sticky="w", column=0, row=1, pady=(0, 2), padx=(4, 10))

        packets_sent_title = Label(self.net_frame, background="white", fg="black", text="Packets sent: ",
                                   font="Arial 12", anchor="w")
        packets_sent_title.grid(sticky="w", column=0, row=2, pady=(0, 2), padx=(4, 10))

        packets_recv_title = Label(self.net_frame, background="white", fg="black", text="Packets received: ",
                                   font="Arial 12", anchor="w")
        packets_recv_title.grid(sticky="w", column=0, row=3, pady=(0, 2), padx=(4, 10))

    def init_net_err_titles(self):
        errin_title = Label(self.net_err_frame, background="white", fg="black", text="Error in: ",
                            font="Arial 12", anchor="w")
        errin_title.grid(sticky="w", column=0, row=0, pady=(0, 2), padx=(4, 10))

        errout_title = Label(self.net_err_frame, background="white", fg="black", text="Error out: ",
                             font="Arial 12", anchor="w")
        errout_title.grid(sticky="w", column=0, row=1, pady=(0, 2), padx=(4, 10))

        dropin_title = Label(self.net_err_frame, background="white", fg="black", text="Dropped in: ",
                             font="Arial 12", anchor="w")
        dropin_title.grid(sticky="w", column=0, row=2, pady=(0, 2), padx=(4, 10))

        dropout_title = Label(self.net_err_frame, background="white", fg="black", text="Dropped out: ",
                              font="Arial 12", anchor="w")
        dropout_title.grid(sticky="w", column=0, row=3, pady=(0, 2), padx=(4, 10))

    def init_net_vals(self):
        self.bytes_sent_val = Label(self.net_frame, background="white", fg="DodgerBlue3",
                                    text=net_info.get_bytes_sent(), font="Arial 12", anchor="e")
        self.bytes_sent_val.grid(sticky="e", column=1, row=0, pady=(0, 2), padx=(40, 4))

        self.bytes_recv_val = Label(self.net_frame, background="white", fg="DodgerBlue3",
                                    text=net_info.get_bytes_recv(), font="Arial 12", anchor="e")
        self.bytes_recv_val.grid(sticky="e", column=1, row=1, pady=(0, 2), padx=(40, 4))

        self.packs_sent_val = Label(self.net_frame, background="white", fg="DodgerBlue3",
                                    text=net_info.get_packs_sent(), font="Arial 12", anchor="e")
        self.packs_sent_val.grid(sticky="e", column=1, row=2, pady=(0, 2), padx=(40, 4))

        self.packs_recv_val = Label(self.net_frame, background="white", fg="DodgerBlue3",
                                    text=net_info.get_packs_recv(), font="Arial 12", anchor="e")
        self.packs_recv_val.grid(sticky="e", column=1, row=3, pady=(0, 2), padx=(40, 4))

    def init_net_err_vals(self):
        self.errin_val = Label(self.net_err_frame, background="white", fg="DodgerBlue3",
                               text=net_info.get_errin(), font="Arial 12", anchor="e")
        self.errin_val.grid(sticky="e", column=1, row=0, pady=(0, 2), padx=(140, 4))

        self.errout_val = Label(self.net_err_frame, background="white", fg="DodgerBlue3",
                                text=net_info.get_errout(), font="Arial 12", anchor="e")
        self.errout_val.grid(sticky="e", column=1, row=1, pady=(0, 2), padx=(140, 4))

        self.dropin_val = Label(self.net_err_frame, background="white", fg="DodgerBlue3",
                                text=net_info.get_drop_in(), font="Arial 12", anchor="e")
        self.dropin_val.grid(sticky="e", column=1, row=2, pady=(0, 2), padx=(140, 4))

        self.dropout_val = Label(self.net_err_frame, background="white", fg="DodgerBlue3",
                                 text=net_info.get_drop_out(), font="Arial 12", anchor="e")
        self.dropout_val.grid(sticky="e", column=1, row=3, pady=(0, 2), padx=(140, 4))

    def update_bytes_sent(self):
        self.bytes_sent_val.configure(text=net_info.get_bytes_sent())

    def update_bytes_recv(self):
        self.bytes_recv_val.configure(text=net_info.get_bytes_recv())

    def update_packs_sent(self):
        self.packs_sent_val.configure(text=net_info.get_packs_sent())

    def update_packs_recv(self):
        self.packs_recv_val.configure(text=net_info.get_packs_recv())

    def update_errin(self):
        self.errin_val.configure(text=net_info.get_errin())

    def update_errout(self):
        self.errout_val.configure(text=net_info.get_errout())

    def update_drop_in(self):
        self.dropin_val.configure(text=net_info.get_drop_in())

    def update_drop_out(self):
        self.dropout_val.configure(text=net_info.get_drop_out())

    def net_updater(self):
        self.update_bytes_sent()
        self.update_bytes_recv()
        self.update_packs_sent()
        self.update_packs_recv()
        self.update_errin()
        self.update_errout()
        self.update_drop_in()
        self.update_drop_out()
        self.master.after(2000, self.net_updater)