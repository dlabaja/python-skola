#!/usr/bin/env python3

import tkinter as tk
from tkinter import HORIZONTAL, TOP, LEFT
from datetime import datetime

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if "textvariable" not in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.timeActive = True
        self.bind("<Escape>", self.quit)
        self.lblMain = tk.Label(self, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.update_time()
        self.btnQuit = tk.Button(self, text="Save & Quit", command=self.quit)
        self.btnClear = tk.Button(self, text="Clear colors", command=self.clearColors)
        self.frameR = tk.Frame(master=self)
        self.frameG = tk.Frame(self)
        self.frameB = tk.Frame(self)
        self.frameMem = tk.Frame(self)

        self.lblR = tk.Label(self.frameR, text="R", width=2)
        self.lblG = tk.Label(self.frameG, text="G", width=2)
        self.lblB = tk.Label(self.frameB, text="B", width=2)

        self.varR = tk.IntVar(value=255)
        self.varR.trace_add("write", self.updateColor)
        self.scaleR = tk.Scale(
            self.frameR,
            from_=0,
            to=255,
            orient=HORIZONTAL,
            length=300,
            variable=self.varR,
        )
        self.entryR = tk.Entry(self.frameR, textvariable=self.varR, width=3)

        self.varG = tk.IntVar(value=255)
        self.varG.trace_add("write", self.updateColor)
        self.scaleG = tk.Scale(
            self.frameG,
            from_=0,
            to=255,
            orient=HORIZONTAL,
            length=300,
            variable=self.varG,
        )
        self.entryG = tk.Entry(self.frameG, textvariable=self.varG, width=3)

        self.varB = tk.IntVar(value=255)
        self.varB.trace_add("write", self.updateColor)
        self.scaleB = tk.Scale(
            self.frameB,
            from_=0,
            to=255,
            orient=HORIZONTAL,
            length=300,
            variable=self.varB,
        )
        self.entryB = tk.Entry(self.frameB, textvariable=self.varB, width=3)

        self.canvas = tk.Canvas(self, background="#ffffff", width=30)
        self.canvas.bind("<Button-1>", self.clickHandler)

        self.lblMain.pack(side=TOP)
        self.frameR.pack(side=TOP)
        self.frameG.pack(side=TOP)
        self.frameB.pack(side=TOP)

        self.lblR.pack(side=LEFT, anchor="s")
        self.scaleR.pack(side=LEFT, anchor="s")
        self.entryR.pack(side=LEFT, anchor="s")

        self.lblG.pack(side=LEFT, anchor="s")
        self.scaleG.pack(side=LEFT, anchor="s")
        self.entryG.pack(side=LEFT, anchor="s")

        self.lblB.pack(side=LEFT, anchor="s")
        self.scaleB.pack(side=LEFT, anchor="s")
        self.entryB.pack(side=LEFT, anchor="s")

        self.canvas.pack(side=TOP, fill="both")
        self.frameMem.pack(side=TOP, fill="both")

        self.lblMain.bind("<Button-1>", self.clickHandlerDate)

        self.canvasList = []
        for row in range(3):
            for col in range(7):
                canvas = tk.Canvas(self.frameMem, width=50, height=50, bg="#ffffff")
                canvas.bind("<Button-1>", self.clickHandler)
                canvas.grid(row=row, column=col)
                self.canvasList.append(canvas)

        self.btnQuit.pack()
        self.btnClear.pack()
        self.load()

    def clickHandlerDate(self, _):
        self.timeActive = not self.timeActive

    def clickHandler(self, event):
        if self.cget("cursor") != "pencil":
            self.config(cursor="pencil")
            self.copycolor = event.widget.cget("background")
        else:
            self.config(cursor="")
            if event.widget is self.canvas:
                r = int(self.copycolor[1:3], 16)
                g = int(self.copycolor[3:5], 16)
                b = int(self.copycolor[5:], 16)
                self.varR.set(r)
                self.varG.set(g)
                self.varB.set(b)
            else:
                event.widget.config(background=self.copycolor)

    def updateColor(self, newvalue=None, neco=None, dalsi=None):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvas.config(background=f"#{r:02X}{g:02X}{b:02X}")

    def quit(self, event=None):
        self.save()
        super().quit()

    def save(self):
        colors = []
        for canvas in self.canvasList:
            colors.append(canvas.cget("background"))

        file = open('latestColors.txt', 'w')
        file.write(str.join("\n", colors))

    def load(self):
        file = open('latestColors.txt', 'r')
        for i, color in enumerate(file.readlines()):
            if self.canvasList[i]:
                self.canvasList[i].config(background=str.replace(color, "\n", ""))

    def clearColors(self):
        for canvas in self.canvasList:
            canvas.config(background="#FFFFFF")

    def update_time(self):
        if self.timeActive:
            time_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.lblMain.config(text=time_string)
        self.after(1000, self.update_time)

app = Application()
app.mainloop()