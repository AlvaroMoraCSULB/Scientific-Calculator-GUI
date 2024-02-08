import tkinter as tk
from tkinter import messagebox
import numpy as np
from numpy import cbrt
import math
import tkinter.messagebox

import unicodedata

calculation=""
euler = 2.7182818
#Pi = 3.141593
class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.sign_toggle_count = 0
        # sets the name on the top of the gui
        self.root.title("Scientific Calculator")
        # sets the background color of the calculator
        # as white
        self.root.configure(background = 'white')

        self.root.geometry("800x500")
        self.menubar = tk.Menu(self.root)
        """to prevent a - dashed line with tearoff """
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        #self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        #self.menubar.add_command(label="Trig", command=)

        self.filemenu.add_separator()
        self.menubar.add_cascade(menu=self.filemenu, label="File")


        self.root.config(menu=self.menubar)
        label = tk.Label(self.root, text="Scientific Calculator", font=('Arial', 14))
        label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=2, font=('Arial', 16),bd=4,width=30, bg="white", fg="black")
        #self.textbox.bind("<KeyPress>", self.textbox.insert("<KeyPress>"))
        self.textbox.pack(padx=20,pady=20,fill=tk.BOTH, expand=True)

        self.check_state = tk.IntVar()
        buttonframe = tk.Frame(self.root)
        buttonframe.columnconfigure(0,minsize= 95, weight=250)
        buttonframe.columnconfigure(1,minsize =95,weight=250)
        buttonframe.columnconfigure(2,minsize= 95, weight=250)
        buttonframe.columnconfigure(3,minsize=95, weight=250)
        buttonframe.columnconfigure(4,minsize= 95, weight=250)

        btn1 = tk.Button(buttonframe, text="\N{SUPERSCRIPT THREE}\u221Ax",font=('Arial', 18),command=self.cubert)
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        btn2 = tk.Button(buttonframe, text=unicodedata.lookup("GREEK SMALL LETTER PI"), font=('Arial', 18),
                         command=lambda: self.add_to_calculation(unicodedata.lookup("GREEK SMALL LETTER PI")))
        btn2.grid(row=0, column=1, sticky=tk.W + tk.E+tk.N+tk.S)

        btn3 = tk.Button(buttonframe, text="e", font=('Arial', 18),command=lambda: self.add_to_calculation("e"))
        btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

        btn4 = tk.Button(buttonframe, text="C", font=('Arial', 18),command=self.clear_field)
        btn4.grid(row=0, column=3, sticky=tk.W + tk.E)

        """btn5 = tk.Button(buttonframe, text="Delete", font=('Arial', 18),command=self.delete)
        btn5.grid(row=0, column=4, sticky=tk.W + tk.E)"""

        btn6 = tk.Button(buttonframe, text="x\N{SUPERSCRIPT TWO}", font=('Arial', 18),command=self.squared)
        btn6.grid(row=1, column=0, sticky=tk.W + tk.E)

        btn7 = tk.Button(buttonframe, text="1/x", font=('Arial', 18),command= self.handle_reciprocal)
        btn7.grid(row=1, column=1, sticky=tk.W + tk.E)

        btn8 = tk.Button(buttonframe, text="|x|", font=('Arial', 18),command=self.absval)
        btn8.grid(row=1, column=2, sticky=tk.W + tk.E)

        btn9 = tk.Button(buttonframe, text="exp", font=('Arial', 18),command=lambda:self.add_to_calculation(" * 10**"))
        btn9.grid(row=1, column=3, sticky=tk.W + tk.E)

        btn10 = tk.Button(buttonframe, text="mod", font=('Arial', 18),command=lambda: self.add_to_calculation(" mod "))
        btn10.grid(row=1, column=4, sticky=tk.W + tk.E)

        btn11 = tk.Button(buttonframe, text="\u00B2\u221Ax", font=('Arial', 18),command=self.squarert)
        btn11.grid(row=2, column=0, sticky=tk.W + tk.E)

        btn12 = tk.Button(buttonframe, text="(", font=('Arial', 18),command=lambda: self.add_to_calculation("("))
        btn12.grid(row=2, column=1, sticky=tk.W + tk.E)

        btn13 = tk.Button(buttonframe, text=")", font=('Arial', 18),command=lambda: self.add_to_calculation(")"))
        btn13.grid(row=2, column=2, sticky=tk.W + tk.E)

        btn14 = tk.Button(buttonframe, text="n!", font=('Arial', 18),command=self.handle_factorial)
        btn14.grid(row=2, column=3, sticky=tk.W + tk.E)

        btn15= tk.Button(buttonframe, text="\u00F7", font=('Arial', 18),command=lambda: self.add_to_calculation("\u00F7"))
        btn15.grid(row=2, column=4, sticky=tk.W + tk.E)

        btn16 = tk.Button(buttonframe, text="x^y", font=('Arial', 18), command=lambda: self.add_to_calculation("^"))
        btn16.grid(row=3, column=0, sticky=tk.W + tk.E)

        btn17 = tk.Button(buttonframe, text="7", font=('Arial', 18),command=lambda: self.add_to_calculation(7))
        btn17.grid(row=3, column=1, sticky=tk.W + tk.E +tk.N+tk.S)

        btn18 = tk.Button(buttonframe, text="8", font=('Arial', 18),command=lambda: self.add_to_calculation(8))
        btn18.grid(row=3, column=2, sticky=tk.W + tk.E+tk.N+tk.S)

        btn19 = tk.Button(buttonframe, text="9", font=('Arial', 18),command=lambda: self.add_to_calculation(9))
        btn19.grid(row=3, column=3, sticky=tk.W + tk.E + tk.N+tk.S)

        btn20 = tk.Button(buttonframe, text="x", font=('Arial', 18),command=lambda: self.add_to_calculation(" x "))
        btn20.grid(row=3, column=4, sticky=tk.W + tk.E+tk.N+tk.S)

        btn21 = tk.Button(buttonframe, text="10^x", font=('Arial', 18),command=self.handle_exponent)
        btn21.grid(row=4, column=0, sticky=tk.W + tk.E)

        btn22 = tk.Button(buttonframe, text="4", font=('Arial', 18),command=lambda: self.add_to_calculation(4))
        btn22.grid(row=4, column=1, sticky=tk.W + tk.E)
        btn23 = tk.Button(buttonframe, text="5", font=('Arial', 18),command=lambda: self.add_to_calculation(5))
        btn23.grid(row=4, column=2, sticky=tk.W + tk.E)
        btn24 = tk.Button(buttonframe, text="6", font=('Arial', 18),command=lambda: self.add_to_calculation(6))
        btn24.grid(row=4, column=3, sticky=tk.W + tk.E)
        btn25 = tk.Button(buttonframe, text="\u2212", font=('Arial', 18),command=lambda: self.add_to_calculation(" - "))
        btn25.grid(row=4, column=4, sticky=tk.W + tk.E)
        btn26 = tk.Button(buttonframe, text="log", font=('Arial', 18),command= self.log10)
        btn26.grid(row=5, column=0, sticky=tk.W + tk.E)
        btn27 = tk.Button(buttonframe, text="1", font=('Arial', 18),command=lambda: self.add_to_calculation(1))
        btn27.grid(row=5, column=1, sticky=tk.W + tk.E)
        btn28 = tk.Button(buttonframe, text="2", font=('Arial', 18),command=lambda: self.add_to_calculation(2))
        btn28.grid(row=5, column=2, sticky=tk.W + tk.E)
        btn29 = tk.Button(buttonframe, text="3", font=('Arial', 18),command=lambda: self.add_to_calculation(3))
        btn29.grid(row=5, column=3, sticky=tk.W + tk.E)
        btn30 = tk.Button(buttonframe, text="+", font=('Arial', 18),command=lambda: self.add_to_calculation(" + "))
        btn30.grid(row=5, column=4, sticky=tk.W + tk.E)
        btn31 = tk.Button(buttonframe, text="ln", font=('Arial', 18),command=self.ln)
        btn31.grid(row=6, column=0, sticky=tk.W + tk.E)
        btn32 = tk.Button(buttonframe, text="+/-", font=('Arial', 18),command=self.toggle_sign)
        btn32.grid(row=6, column=1, sticky=tk.W + tk.E)
        btn33= tk.Button(buttonframe, text="0", font=('Arial', 18),command=lambda: self.add_to_calculation(0))
        btn33.grid(row=6, column=2, sticky=tk.W + tk.E)
        btn34 = tk.Button(buttonframe, text=".", font=('Arial', 18),command=lambda: self.add_to_calculation("."))
        btn34.grid(row=6, column=3, sticky=tk.W + tk.E)
        btn35 = tk.Button(buttonframe, text="=", font=('Arial', 18),command=self.evaluate_calculation)
        btn35.grid(row=6, column=4, sticky=tk.W + tk.E)

        """fill = 'x' going to stretch on the x- dimension
        fill = tk.both going to stretch it on the x and y dimension"""
        buttonframe.pack(fill=tk.BOTH)
        self.root.mainloop()
    def show_message(self):
       if self.check_state.get() == 0:
           print(self.textbox.get('1.0',tk.END))
       else:
           messagebox.showinfo(title="Message",message=self.textbox.get('1.0', tk.END))
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
            self.root.destroy()
    def delete(self):
        previous_text = self.textbox.get("1.0", tk.END)
        current_text = self.textbox.get("1.0", tk.END)[:-2]  # Exclude the newline character
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert("1.0", current_text)

    def clear_field(self):
        global calculation
        calculation =""
        self.textbox.delete(1.0, "end")
    def add_to_calculation(self,symbol):
        global calculation
        if symbol == " * 10**":
            calculation += f"{symbol}"
        else:
            calculation += str(symbol)
        #calculation += str(symbol)
        self.textbox.delete(1.0, "end")
        self.textbox.insert(1.0, calculation)
    def evaluate_calculation(self):
        global calculation
        try:
            if "mod" in calculation:
                calculation=calculation.replace("mod","%")
                pi = unicodedata.lookup("GREEK SMALL LETTER PI")
                e = "e"
                if pi in calculation:
                    calculation = calculation.replace(pi, str(math.pi))  # Fix: Replace pi with its numerical value
                if e in calculation:
                    calculation= calculation.replace(e, str(euler))
                result = eval(calculation)
            elif 'x' in calculation:
                calculation = calculation.replace("x", "*")
                pi = unicodedata.lookup("GREEK SMALL LETTER PI")
                e = "e"
                if pi in calculation:
                    calculation = calculation.replace(pi, str(math.pi))  # Fix: Replace pi with its numerical value
                result = eval(calculation)
            elif '\u00F7' in calculation:
                calculation = calculation.replace("\u00F7", "/")
                pi = unicodedata.lookup("GREEK SMALL LETTER PI")
                e = "e"
                if pi in calculation:
                    calculation = calculation.replace(pi, str(math.pi))  # Fix: Replace pi with its numerical value
                if e in calculation:
                    calculation= calculation.replace(e, str(euler))
                result = eval(calculation)
            elif "^" in calculation:
                calculation = calculation.replace("^", "**")
                pi = unicodedata.lookup("GREEK SMALL LETTER PI")
                e = "e"
                if pi in calculation:
                    calculation = calculation.replace(pi, str(math.pi))  # Fix: Replace pi with its numerical value
                if e in calculation:
                    calculation = calculation.replace(e, str(euler))
                result = eval(calculation)
            else:
                pi = unicodedata.lookup("GREEK SMALL LETTER PI")
                e = "e"
                if pi in calculation:
                    calculation = calculation.replace(pi, str(math.pi))  # Fix: Replace pi with its numerical value
                if e in calculation:
                    calculation= calculation.replace(e, str(euler))
                result = eval(calculation)
            calculation = str(result)
            self.textbox.delete("1.0", tk.END)
            self.textbox.insert("1.0", calculation)
        except ZeroDivisionError:
            self.clear_field()
            self.textbox.insert("1.0", "Error: Undefined")
        except:
            self.clear_field()
            self.textbox.insert("1.0", "Error")


    def handle_reciprocal(self):
        global calculation
        try:
         # Evaluate the current expression and calculate the reciprocal
         calculation = str(eval(calculation))
         result = 1 / int(calculation)
         self.textbox.delete(1.0,"end")
         self.textbox.insert(1.0,f"1/({calculation}) = {str(result)}")
         calculation = str(result)
        except ZeroDivisionError:
            self.clear_field()
            self.textbox.insert(1.0, "Error: Undefined")
    def handle_exponent(self):
        global calculation
        try:
            calculation = str(eval(calculation))
            result = pow(10,int(calculation))
            self.textbox.delete(1.0, "end")
            self.textbox.insert(1.0,f"10^{calculation} = {str(result)}")
            calculation = str(result)
        except:
            self.clear_field()
            self.textbox.insert(1.0, "Error")
    def squared(self):
        global calculation
        try:
            calculation = str(eval(calculation))
            result = pow(int(calculation), 2)
            self.textbox.delete(1.0, "end")
            self.textbox.insert(1.0, str(result))
        except:
            self.clear_field()
            self.textbox.insert(1.0, "Error")
    def squarert(self):
        global calculation
        try:
            calculation = str(eval(calculation))
            result = math.sqrt(float(calculation))
            self.textbox.delete(1.0, "end")
            self.textbox.insert(1.0,f"\u221A{calculation} = {str(result)}")
            calculation = str(result)
        except:
            self.clear_field()
            self.textbox.insert(1.0, "Error")
    def cubert(self):
        global calculation
        try:
            calculation = str(eval(calculation))
            list = []
            list.append(float(calculation))
            result =  np.cbrt(list)[0]
            self.textbox.delete(1.0, "end")
            self.textbox.insert(1.0,f"cuberoot({calculation}) = {str(result)}")
            calculation = str(result)
        except:
            self.clear_field()
            self.textbox.insert(1.0, "Error")
    def handle_factorial(self):
        global calculation
        try:
            n = int(eval(calculation))
            result = self.calculate_factorial(n)
            self.textbox.delete(1.0, "end")
            self.textbox.insert(1.0,f"fact({n}) = {str(result)}")
            calculation = str(result)
        except:
            self.clear_field()
            self.textbox.insert(1.0, "Error")

    def calculate_factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)
    def absval(self):
        global calculation
        try:
            n = float(eval(calculation))
            result = abs(n)
            self.textbox.delete(1.0, "end")
            self.textbox.insert(1.0,f"abs({n}) = {str(result)}")
            calculation = str(result)
        except ValueError:
            self.clear_field()
            self.textbox.insert(1.0, "Error")
    def log10(self):
        global calculation
        try:
            n = int(eval(calculation))
            result = math.log10(n)
            self.textbox.delete(1.0, "end")
            self.textbox.insert(1.0,f"log\u2081\u2080({n}) = {str(result)}")
            calculation = str(result)
        except ValueError:
            self.clear_field()
            self.textbox.insert(1.0, "Invalid Input")
    def ln(self):
        global calculation
        try:
            n = float(eval(calculation))
            result = math.log10(n)/math.log10(euler)
            self.textbox.delete(1.0, "end")
            self.textbox.insert(1.0,f"ln({n}) = {str(result)}")
            calculation = str(result)
        except ValueError:
            self.clear_field()
            self.textbox.insert(1.0, "Invalid Input")


    def toggle_sign(self):
        global calculation
        if self.sign_toggle_count % 2 == 0:
            # If the count is even, add a negative sign
            calculation = "-" + calculation
        else:
            # If the count is odd, remove the negative sign
            calculation = calculation[1:]
            #calcultation = "+" + calculation

        self.sign_toggle_count += 1

        self.textbox.delete(1.0, "end")
        self.textbox.insert(1.0, calculation)



Calculator()
