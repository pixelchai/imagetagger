import tkinter as tk

class Tagger(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.master.title("ImageTagger")
        self.master.geometry("960x540")
        # self.master.state('zoomed')

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
