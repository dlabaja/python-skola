import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
from grafy import *

class GrafApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graf funkce")

        # Frame for function graph generation
        frame1 = tk.LabelFrame(root, text="Generuj graf funkce")
        frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Radio buttons for function selection
        self.function_var = tk.StringVar(value="sin")
        tk.Radiobutton(frame1, text="sin", variable=self.function_var, value="sin").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(frame1, text="cos", variable=self.function_var, value="cos").grid(row=1, column=0, sticky="w")
        tk.Radiobutton(frame1, text="log", variable=self.function_var, value="log").grid(row=2, column=0, sticky="w")
        tk.Radiobutton(frame1, text="exp", variable=self.function_var, value="exp").grid(row=3, column=0, sticky="w")

        # Entry fields for range
        tk.Label(frame1, text="Od").grid(row=0, column=1)
        self.range_from = tk.Entry(frame1)
        self.range_from.grid(row=0, column=2)

        tk.Label(frame1, text="Do").grid(row=1, column=1)
        self.range_to = tk.Entry(frame1)
        self.range_to.grid(row=1, column=2)

        # Button to generate graph
        tk.Button(frame1, text="Vytvoř graf", command=self.generate_function_graph).grid(row=4, column=0, columnspan=3, pady=5)

        # Frame for graph from text file
        frame2 = tk.LabelFrame(root, text="Generuj graf z textových dat")
        frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Entry and button to select file
        self.file_path = tk.Entry(frame2)
        self.file_path.grid(row=0, column=0, padx=5, pady=5)

        tk.Button(frame2, text="Vyber soubor", command=self.select_file).grid(row=0, column=1, padx=5, pady=5)

        # Button to generate graph from file
        tk.Button(frame2, text="Vytvoř graf", command=self.generate_file_graph).grid(row=1, column=0, columnspan=2, pady=5)

        # Frame for axis labels
        frame3 = tk.LabelFrame(root, text="Popisky os")
        frame3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Entry fields for axis labels
        tk.Label(frame3, text="osa X").grid(row=0, column=0)
        self.axis_x = tk.Entry(frame3)
        self.axis_x.grid(row=0, column=1)

        tk.Label(frame3, text="osa Y").grid(row=1, column=0)
        self.axis_y = tk.Entry(frame3)
        self.axis_y.grid(row=1, column=1)

    def generate_function_graph(self):
        if not self.can_parse_string(self.range_from.get()) or not self.can_parse_string(self.range_to.get()):
            messagebox.showerror(title='Chybné meze', message='Zadejte meze osy X\njako reálná čísla')
            return

        x = np.linspace(float(self.range_from.get()), float(self.range_to.get()), 500)
        axis = (self.axis_x.get(), self.axis_y.get())

        match self.function_var.get():
            case "sin":
                return draw_sinus(axis, x)
            case "cos":
                return draw_cosinus(axis, x)
            case "log":
                return draw_logarithm(axis, x)
            case "exp":
                return draw_exponential(axis, x)

    def can_parse_string(self, text):
        print(text)
        try:
            number = float(text)
            return True
        except:
            return False

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.delete(0, tk.END)
            self.file_path.insert(0, file_path)

    def generate_file_graph(self):
        try:
            path = self.file_path.get()
            if not path:
                raise FileNotFoundError("Nebyla zadána cesta k souboru.")
            x, y = self.read_file(path)
            axis = (self.axis_x.get(), self.axis_y.get())
            
            draw_custom_graph(axis, x, y)
        
        except Exception as e:
            messagebox.showerror(title='Chybný formát souboru', 
                message='Graf se nepodařilo vytvořit,\nzkontrolujte fomát souboru.')

    def read_file(self, cesta):
        x = []
        y = []

        with open(cesta, 'r') as f:
            for row in f:
                nums = row.split()
                if len(nums) != 2:
                    raise ValueError(f"Neplatný formát dat v souboru na řádku: {row.strip()}")

                x.append(float(nums[0]))
                y.append(float(nums[1]))
        
        return x, y


# Create the main application window
root = tk.Tk()
app = GrafApp(root)
root.mainloop()
