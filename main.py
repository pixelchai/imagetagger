import tkinter as tk
import ui

if __name__ == '__main__':
    root = tk.Tk()

    root.title("ImageTagger")
    root.state('zoomed')

    app = ui.Tagger(root)
    app.mainloop()
