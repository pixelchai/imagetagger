import tkinter as tk

class Tagger(tk.Frame):
    def __int__(self, master):
        super().__init__(master)
        self.master = master

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass
