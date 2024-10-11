import tkinter as tk
from tkinter import StringVar, ttk
import math
import re
from collections import deque


class PostfixCalculator:
    def __init__(self):
        self._buffer = deque()
        self._operations = {}
        self._exception_message = "Invalid Syntax"
        self.init_dict()

    def init_dict(self):
        self._operations = {
            "+": lambda: self._buffer.pop() + self._buffer.pop(),
            "-": lambda: self._buffer.pop() - self._buffer.pop(),
            "*": lambda: self._buffer.pop() * self._buffer.pop(),
            "/": lambda: self.divide(),
            "%": lambda: self._buffer.pop() % self._buffer.pop(),
            "sin": lambda: math.sin(self._buffer.pop()),
            "cos": lambda: math.cos(self._buffer.pop()),
            "tg": lambda: math.tan(self._buffer.pop()),
            "cotg": lambda: self.cotg(),
            "pow": lambda: math.pow(self._buffer.pop(), 2),
            "sqrt": lambda: self.sqrt(),
            "log": lambda: self.log10(),
            "ln": lambda: self.ln(),
            "abs": lambda: abs(self._buffer.pop()),
            "π": lambda: math.pi,
            "e": lambda: math.e
        }

    def divide(self):
        num2 = self._buffer.pop()
        num1 = self._buffer.pop()
        if num2 == 0:
            self.throw_exception("Cannot divide by zero")
        return num1 / num2

    def cotg(self):
        num = self._buffer.pop()
        if num == 0:
            self.throw_exception("Cotg() cannot be zero")
        return math.cos(num) / math.sin(num)

    def sqrt(self):
        num = self._buffer.pop()
        if num < 0:
            self.throw_exception("Sqrt() cannot be < 0")
        return math.sqrt(num)

    def log10(self):
        num = self._buffer.pop()
        if num <= 0:
            self.throw_exception("Log() cannot be ≤ 0")
        return math.log10(num)

    def ln(self):
        num = self._buffer.pop()
        if num <= 0:
            self.throw_exception("Ln() cannot be ≤ 0")
        return math.log(num)

    def calculate_postfix(self, commands):
        try:
            self.init_dict()
            for item in commands:
                if str(item) in self._operations:
                    self._buffer.append(self._operations[str(item)]())
                else:
                    self._buffer.append(float(item))
            if len(self._buffer) > 1:
                raise Exception()  # more than one number in result
        except Exception:
            return self._exception_message

        return self._buffer.pop()

    def throw_exception(self, msg):
        self._exception_message = msg
        raise Exception()

    def infix_to_postfix(self, infix):
        self.init_dict()
        postfix = []
        stack = deque()

        # replace constants
        infix = infix.replace("π", str(math.pi))
        infix = infix.replace("e", str(math.e))

        # fix for negative numbers
        if infix[0] == '-':
            infix = '0' + infix
        infix = re.sub(r'\(-', '(0-', infix)

        tokens = re.findall(r'[+\%\-\*\/()]|\d*\.?\d+|[a-z]+', infix)

        for item in tokens:
            if item == "(":  # start of stack region
                stack.append("(")
            elif re.match(r'\d*\.?\d+', item):  # number
                postfix.append(float(item))
            elif item == ")":  # pop stack to 14_postfix until '('
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                if stack:
                    stack.pop()
            else:  # operator/function
                while stack and stack[-1] != "(" and self.get_precedence(stack[-1]) >= self.get_precedence(item):
                    postfix.append(stack.pop())
                stack.append(item)

        while stack:  # empty stack
            postfix.append(stack.pop())

        return postfix

    @staticmethod
    def get_precedence(op):
        if op in ["+", "-"]:
            return 1
        elif op in ["*", "/", "%"]:
            return 2
        else:
            return 3


class CalculatorApp:
    def __init__(self, root):
        self.calculator = PostfixCalculator()

        self.root = root
        self.root.title("Postfix Calculator")
        self.root.geometry("400x300")

        self.result_var = StringVar()
        self.input_var = StringVar()

        # Result label
        self.result_label = ttk.Label(self.root, textvariable=self.result_var, font=("Helvetica", 16), anchor="center")
        self.result_label.pack(pady=10)

        # Input field
        self.input_entry = ttk.Entry(self.root, textvariable=self.input_var, font=("Helvetica", 14), justify='center')
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<Return>", self.calculate_result)

    def calculate_result(self, event):
        try:
            infix_expr = self.input_var.get()
            postfix_expr = self.calculator.infix_to_postfix(infix_expr)
            result = self.calculator.calculate_postfix(postfix_expr)
            self.result_var.set(f"Result: {result}")
        except Exception as e:
            self.result_var.set(f"Error: {str(e)}")

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()