import tkinter as tk
from tkinter import ttk, messagebox
import requests
import math
import datetime as dt
import os
from .about import About
from .entry import MyEntry


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.fee = 4
        self.feemod = 1
        self.title("$měnárna")
        self.bind("<Escape>", self.quit)

        self.varAuto = tk.BooleanVar()
        self.currency = tk.StringVar()
        self.ammount = tk.StringVar()
        self.rate = tk.StringVar()
        self.exrate = {}
        self.input = tk.IntVar()
        self.output = tk.IntVar()

        self.tickFrame = tk.LabelFrame(self, text="Kurzovní lístek")
        self.tickState = tk.Label(self.tickFrame, text="Stav kurzovního lístku")
        self.tickState.pack()
        self.chboxAuto = tk.Checkbutton(
            self.tickFrame,
            text="Automaticky stahovat kurzovní lístek",
            variable=self.varAuto,
            command=self.chbtnAutoClick,
        )
        self.btnDownload = tk.Button(
            self.tickFrame, text="Stáhnout kurzovní lístek", command=self.download
        )
        self.tickFrame.pack(anchor="w", padx=5)
        self.chboxAuto.pack()
        self.btnDownload.pack()

        self.lblFrame = tk.LabelFrame(self, text="Transakce")
        self.lblFrame.pack(anchor="w", padx=5)
        self.varTransaction = tk.StringVar()
        self.varTransaction.set("None")
        self.rbtnPurchase = tk.Radiobutton(
            self.lblFrame, value="purchase", variable=self.varTransaction, text="Nákup", command=self.changeTransaction
        )
        self.rbtnPurchase.pack()
        self.rbtnSale = tk.Radiobutton(
            self.lblFrame, text="Prodej", variable=self.varTransaction, value="sale", command=self.changeTransaction
        )
        self.rbtnSale.pack()

        self.currFrame = tk.LabelFrame(self, text="Měna")
        self.currFrame.pack(anchor="w", padx=5)
        self.combo = ttk.Combobox(self.currFrame, textvariable=self.currency)
        self.combo["values"] = "Nenalezeno!"
        self.combo.current(0)
        self.combo.pack()
        self.combo.bind("<<ComboboxSelected>>", self.on_select)

        self.rateFrame = tk.LabelFrame(self, text="Kurz")
        self.amLabel = tk.Label(self.rateFrame, text="UNKNOWN")
        self.raLabel = tk.Label(self.rateFrame, text="CZK")
        self.entryAmmount = MyEntry(self.rateFrame, textvariable=self.ammount, state="readonly")
        self.entryRate = MyEntry(self.rateFrame, textvariable=self.rate, state="readonly")
        self.rateFrame.pack(anchor="w", padx=5)
        self.entryAmmount.grid(row=0)
        self.amLabel.grid(row=0, column=1)
        self.entryRate.grid(row=1)
        self.raLabel.grid(row=1, column=1)

        self.calcFrame = tk.LabelFrame(self, text="Výpočet")
        self.calcInput = MyEntry(self.calcFrame, textvariable=self.input)
        self.calcBtn = tk.Button(self.calcFrame, text="Výpočet", state="disabled", command=self.calculate)
        self.calcOutput = MyEntry(self.calcFrame, textvariable=self.output, state="readonly")
        self.inLabel = tk.Label(self.calcFrame, text="UNKNOWN")
        self.ouLabel = tk.Label(self.calcFrame, text="CZK")
        self.calcFrame.pack(anchor="w", padx=5)
        self.calcInput.grid(row=0, column=0)
        self.inLabel.grid(row=0, column=1)
        self.calcBtn.grid(row=2, column=0)
        self.calcOutput.grid(row=1, column=0)
        self.ouLabel.grid(row=1, column=1)

        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="About", command=self.about)
        self.btn2.pack()

        self.ammount.set('')

        # Load settings and check for auto download
        if os.path.exists("settings.txt"):
            with open("settings.txt", "r") as f:
                if f.read() == "1":
                    self.varAuto.set(True)
                    self.btnDownload.config(state="disabled")
                else:
                    self.varAuto.set(False)
                f.close()
        else:
            pass
        if self.varAuto.get():
            self.download()
        if os.path.exists("kurzovni_listek.txt"):
            with open("kurzovni_listek.txt", "r") as f:
                date_line = f.readline()
                data = f.read()
                f.close()
            self.load_ticket(data)
            self.load_date(date_line)

    def load_date(self, file_date):
        date = dt.datetime.now()
        self.tickState.configure(text=f"{file_date[:2]} {file_date[3:6]} {file_date[7:12]}")
        if int(file_date[:2]) < date.day - 1 or file_date[3:6] != date.strftime("%b") or int(file_date[7:12]) != date.year:
            self.tickState.config(bg="red")
            messagebox.showwarning(title="Lístek není aktuální",
                                   message="Váš kurzovní lístek není aktuální,\n pokračujte na vlastní nebezpečí!")
        else:
            self.tickState.config(bg="green")

    def on_select(self, event=None):
        self.output.set(0)
        selected = self.currency.get()
        if self.exrate == {}:
            pass
        else:
            try:
                info = self.exrate[selected]
                self.ammount.set(info[0])
                self.rate.set(info[1] * self.feemod)
                self.amLabel.config(text=info[2])
                self.inLabel.config(text=info[2])
            except KeyError:
                pass
            if (
                    self.varTransaction.get() == "purchase" or self.varTransaction.get() == "sale") and self.ammount.get() != '':
                self.calcBtn.config(state="normal")

    def changeTransaction(self):
        self.output.set(0)
        if self.varTransaction.get() == "purchase":
            self.feemod = 1 - (0.01 * self.fee)
        else:
            self.feemod = 1 + (0.01 * self.fee)
        self.on_select(None)
        if self.exrate != {} and self.ammount.get() != '':
            self.calcBtn.config(state="normal")

    def calculate(self):
        if self.varTransaction.get() == "purchase":
            self.output.set(math.floor((self.input.get() / float(self.ammount.get())) * float(self.rate.get())))
        elif self.varTransaction.get() == "sale":
            self.output.set(math.ceil((self.input.get() / float(self.ammount.get())) * float(self.rate.get())))

    def chbtnAutoClick(self):
        with open("settings.txt", "w") as f:
            if self.varAuto.get():
                self.btnDownload.configure(state="disabled")
                f.write("1")
            else:
                f.write("0")
                self.btnDownload.configure(state="normal")

    def about(self):
        window = About(self)
        window.grab_set()

    def quit(self, event=None):
        super().quit()

    def load_ticket(self, ticket):
        for line in ticket.splitlines()[2:]:
            country, currency, amount, code, rate = line.split("|")
            self.exrate[f"{country}({code})"] = [float(amount), float(rate), str(code)]
        self.combo.config(values=list(self.exrate.keys()))

    def download(self):
        url = "https://www.cnb.cz/en/financial_markets/foreign_exchange_market/exchange_rate_fixing/daily.txt"
        try:
            response = requests.get(url)
            data = response.text
            with open("kurzovni_listek.txt", "w") as f:
                f.write(data)
        except requests.exceptions.ConnectionError as e:
            print(f"Error: {e}")
            messagebox.showerror(
                message=f"Nebylo možné stáhnout kurzovní lístek.\nZkontrolujte připojení k internetu.\n Kód chyby: {e}",
                title="Chyba stahování")

        if os.path.exists("kurzovni_listek.txt"):
            with open("kurzovni_listek.txt", "r") as f:
                date_info = f.readline()
                data = f.read()
                f.close()
        else:
            print("Critical error!")
            self.destroy()
        self.load_ticket(data)
        self.load_date(date_info)
