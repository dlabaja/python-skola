import tkinter as tk


class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.config()

        self.lbl = tk.Label(self, text="to nebylo moc skibidi")
        self.btn = tk.Button(self, text="OK", command=self.close)

        self.lbl.pack()
        self.btn.pack()

    def close(self):
        self.destroy()
