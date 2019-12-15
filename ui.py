import tkinter as tk
from PIL import ImageTk, Image

class Tagger(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.master.title("ImageTagger")
        self.master.geometry("960x540")
        # self.master.state('zoomed')

        self.img = ImageTk.PhotoImage(Image.open("res/loading.png"))
        self.panel = tk.Label(master, image=self.img, height=20)
        self.panel.grid(row=0, column=0)

        # f = tk.Frame(master, height=32, width=tk.)
        # f.pack_propagate(0)  # don't shrink
        # f.pack()

        button = tk.Button(self, text="LOL").grid(row=1, column=0)
        button = tk.Button(self, text="LOL").grid(row=1, column=1)

        # self.pack()
