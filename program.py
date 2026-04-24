from tkinter import *
from tkinter import ttk

window = Tk() # creating window
label_text="0"
first = 0
second = 0

window.title("Calculator") # naming window
window.geometry("500x400") # set window's resolution

window.update_idletasks()
window.resizable(False, False)

# creating grid
for c in range(4): window.columnconfigure(index=c, weight=1)
for r in range(5): window.rowconfigure(index=r, weight=1)

label = ttk.Label(text=label_text)
label.grid(row=0, column=0, columnspan=2, ipadx=30, ipady=30, padx=5, pady=5)

deletebtn = ttk.Button(text="Delete")
deletebtn.grid(row=0, column=2, ipadx=20, ipady=20, padx=2, pady=2)

btn1 = ttk.Button(text="1")
btn1.grid(row=3, column=0, ipadx=20, ipady=20, padx=2, pady=2)

btn2 = ttk.Button(text="2")
btn2.grid(row=3, column=1, ipadx=20, ipady=20, padx=2, pady=2)

btn3 = ttk.Button(text="3")
btn3.grid(row=3, column=2, ipadx=20, ipady=20, padx=2, pady=2)

btn4 = ttk.Button(text="4")
btn4.grid(row=2, column=0, ipadx=20, ipady=20, padx=2, pady=2)

btn5 = ttk.Button(text="5")
btn5.grid(row=2, column=1, ipadx=20, ipady=20, padx=2, pady=2)

btn6 = ttk.Button(text="6")
btn6.grid(row=2, column=2, ipadx=20, ipady=20, padx=2, pady=2)

btn7 = ttk.Button(text="7")
btn7.grid(row=1, column=0, ipadx=20, ipady=20, padx=2, pady=2)

btn8 = ttk.Button(text="8")
btn8.grid(row=1, column=1, ipadx=20, ipady=20, padx=2, pady=2)

btn9 = ttk.Button(text="9")
btn9.grid(row=1, column=2, ipadx=20, ipady=20, padx=2, pady=2)

btn0 = ttk.Button(text="0")
btn0.grid(row=4, column=0, columnspan=3, ipadx=150, ipady=20, padx=2, pady=2)

btn9 = ttk.Button(text="+")
btn9.grid(row=4, column=3, ipadx=20, ipady=20, padx=2, pady=2)

btn9 = ttk.Button(text="-")
btn9.grid(row=3, column=3, ipadx=20, ipady=20, padx=2, pady=2)

btn9 = ttk.Button(text="+")
btn9.grid(row=4, column=3, ipadx=20, ipady=20, padx=2, pady=2)

btn9 = ttk.Button(text="*")
btn9.grid(row=2, column=3, ipadx=20, ipady=20, padx=2, pady=2)

btn9 = ttk.Button(text="/")
btn9.grid(row=1, column=3, ipadx=20, ipady=20, padx=2, pady=2)

btn9 = ttk.Button(text="=")
btn9.grid(row=0, column=3, ipadx=20, ipady=20, padx=2, pady=2)

window.mainloop()