from tkinter import *
from tkinter import ttk

window = Tk() # creating window
label_text = "0"
first = 0
second = 0
operation = None

window.title("Calculator") # naming window
window.geometry("500x400") # set window's resolution

window.update_idletasks()
window.resizable(False, False)

# creating grid
for c in range(4): window.columnconfigure(index=c, weight=1)
for r in range(5): window.rowconfigure(index=r, weight=1)

label = ttk.Label(text=label_text, font=("Arial", 16))
label.grid(row=0, column=0, columnspan=3, ipadx=30, ipady=30, padx=5, pady=5)

# ===== FUNCTIONS =====
def on_number_click(num):
    current = label.cget("text")
    if current == "0":
        label.config(text=str(num))
    else:
        label.config(text=current + str(num))

def on_operator_click(op):
    global first, operation
    first = float(label.cget("text"))
    operation = op
    label.config(text="0")

def on_equals_click():
    global first, second, operation
    second = float(label.cget("text"))
    result = 0
    
    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        if second != 0:
            result = first / second
        else:
            label.config(text="Error")
            return
    
    label.config(text=str(result))

def on_delete_click():
    label.config(text="0")

def on_decimal_click():
    current = label.cget("text")
    if "." not in current:
        label.config(text=current + ".")

# ===== BUTTONS =====
deletebtn = ttk.Button(text="Clear", command=on_delete_click)
deletebtn.grid(row=0, column=2, ipadx=20, ipady=20, padx=2, pady=2)

# Number buttons
btn1 = ttk.Button(text="1", command=lambda: on_number_click(1))
btn1.grid(row=3, column=0, ipadx=20, ipady=20, padx=2, pady=2)

btn2 = ttk.Button(text="2", command=lambda: on_number_click(2))
btn2.grid(row=3, column=1, ipadx=20, ipady=20, padx=2, pady=2)

btn3 = ttk.Button(text="3", command=lambda: on_number_click(3))
btn3.grid(row=3, column=2, ipadx=20, ipady=20, padx=2, pady=2)

btn4 = ttk.Button(text="4", command=lambda: on_number_click(4))
btn4.grid(row=2, column=0, ipadx=20, ipady=20, padx=2, pady=2)

btn5 = ttk.Button(text="5", command=lambda: on_number_click(5))
btn5.grid(row=2, column=1, ipadx=20, ipady=20, padx=2, pady=2)

btn6 = ttk.Button(text="6", command=lambda: on_number_click(6))
btn6.grid(row=2, column=2, ipadx=20, ipady=20, padx=2, pady=2)

btn7 = ttk.Button(text="7", command=lambda: on_number_click(7))
btn7.grid(row=1, column=0, ipadx=20, ipady=20, padx=2, pady=2)

btn8 = ttk.Button(text="8", command=lambda: on_number_click(8))
btn8.grid(row=1, column=1, ipadx=20, ipady=20, padx=2, pady=2)

btn9 = ttk.Button(text="9", command=lambda: on_number_click(9))
btn9.grid(row=1, column=2, ipadx=20, ipady=20, padx=2, pady=2)

btn0 = ttk.Button(text="0", command=lambda: on_number_click(0))
btn0.grid(row=4, column=0, columnspan=2, ipadx=75, ipady=20, padx=2, pady=2)

# Decimal point
btn_decimal = ttk.Button(text=".", command=on_decimal_click)
btn_decimal.grid(row=4, column=2, ipadx=20, ipady=20, padx=2, pady=2)

# Operator buttons
btn_plus = ttk.Button(text="+", command=lambda: on_operator_click("+"))
btn_plus.grid(row=4, column=3, ipadx=20, ipady=20, padx=2, pady=2)

btn_minus = ttk.Button(text="-", command=lambda: on_operator_click("-"))
btn_minus.grid(row=3, column=3, ipadx=20, ipady=20, padx=2, pady=2)

btn_multiply = ttk.Button(text="*", command=lambda: on_operator_click("*"))
btn_multiply.grid(row=2, column=3, ipadx=20, ipady=20, padx=2, pady=2)

btn_divide = ttk.Button(text="/", command=lambda: on_operator_click("/"))
btn_divide.grid(row=1, column=3, ipadx=20, ipady=20, padx=2, pady=2)

btn_equals = ttk.Button(text="=", command=on_equals_click)
btn_equals.grid(row=0, column=3, ipadx=20, ipady=20, padx=2, pady=2)

window.mainloop()