from _ast import Lambda
from tkinter import *
from tkinter.font import *

calculator = Tk()

# giving title
calculator.title("Basic Calculator")
# inserting icon
calculator.iconbitmap('/Users/user/Desktop/ComputingLab1/Calculator App/calculator_icon.ico')
# defining the font
myFont = Font(size=25, weight="bold")
nextFont = Font(size=22)

screenEntry = Entry(calculator, width=27, borderwidth=5)
screenEntry.grid(row=0, column=0, columnspan=5, padx=15, pady=15, ipadx=20, ipady=20)
screenEntry['font'] = nextFont
# functions


def button_click_number(number):
    currentDisplay = screenEntry.get()
    screenEntry.delete(0, END)
    screenEntry.insert(0, str(currentDisplay) + str(number))


def button_click_equal():
    secondNumber = screenEntry.get()
    screenEntry.delete(0, END)


def button_click_delete():  # need to be changed
    screenEntry.delete(0, END)


def button_click_allClear():
    screenEntry.delete(0, END)


def button_click_equal():  # need to be changed
    screenEntry.delete(0, END)
# Creating digit buttons and entry fields

button_click_pi = Button(calculator, text="π", padx=25, pady=8, highlightbackground="yellow", fg="black", command=lambda: button_click_number('π'))
button_click_pi.grid(row=2, column=0)
button_click_pi['font'] = myFont
button_click_percentage = Button(calculator, text="%", padx=25, pady=8, highlightbackground="#FFFF00", fg="black", command=lambda: button_click_number('%'))
button_click_percentage.grid(row=2, column=1)
button_click_percentage['font'] = myFont
button_click_modulo = Button(calculator, text="MOD", padx=4, pady=8, highlightbackground="yellow", fg="#000000", command=lambda: button_click_number('MOD'))
button_click_modulo.grid(row=2, column=2)
button_click_modulo['font'] = myFont



button_click_0 = Button(calculator, text="0", padx=25, pady=8, highlightbackground="black", fg="#FFFFFF", command=lambda: button_click_number(0))
button_click_0.grid(row=9, column=0)
button_click_0['font'] = myFont
button_click_point = Button(calculator, text=".", padx=28, pady=8, highlightbackground="red", fg="#000000", command=lambda: button_click_number('.'))
button_click_point.grid(row=9, column=1)
button_click_point['font'] = myFont
button_click_00 = Button(calculator, text="00", padx=18, pady=8, highlightbackground="#000000", fg="#FFFFFF", command=lambda: button_click_number("00"))
button_click_00.grid(row=9, column=2)
button_click_00['font'] = myFont

button_click_1 = Button(calculator, text="1", padx=25, pady=8, highlightbackground="black", fg="white", command=lambda: button_click_number(1))
button_click_1.grid(row=8, column=0)
button_click_1['font'] = myFont
button_click_2 = Button(calculator, text="2", padx=25, pady=8, highlightbackground="black", fg="white", command=lambda: button_click_number(2))
button_click_2.grid(row=8, column=1)
button_click_2['font'] = myFont
button_click_3 = Button(calculator, text="3", padx=25, pady=8, highlightbackground="black", fg="white", command=lambda: button_click_number(3))
button_click_3.grid(row=8, column=2)
button_click_3['font'] = myFont

button_click_4 = Button(calculator, text="4", padx=25, pady=8, highlightbackground="black", fg="white", command=lambda: button_click_number(4))
button_click_4.grid(row=6, column=0)
button_click_4['font'] = myFont
button_click_5 = Button(calculator, text="5", padx=25, pady=8, highlightbackground="black", fg="white", command=lambda: button_click_number(5))
button_click_5.grid(row=6, column=1)
button_click_5['font'] = myFont
button_click_6 = Button(calculator, text="6", padx=25, pady=8, highlightbackground="black", fg="white", command=lambda: button_click_number(6))
button_click_6.grid(row=6, column=2)
button_click_6['font'] = myFont


button_click_7 = Button(calculator, text="7", padx=25, pady=8, highlightbackground="#000000", fg="#FFFFFF", command=lambda: button_click_number(7))
button_click_7.grid(row=4, column=0)
button_click_7['font'] = myFont
button_click_8 = Button(calculator, text="8", padx=25, pady=8, highlightbackground="#000000", fg="#FFFFFF", command=lambda: button_click_number(8))
button_click_8.grid(row=4, column=1)
button_click_8['font'] = myFont
button_click_9 = Button(calculator, text="9", padx=25, pady=8, highlightbackground="#000000", fg="#FFFFFF", command=lambda: button_click_number(9))
button_click_9.grid(row=4, column=2)
button_click_9['font'] = myFont

# Clearing the screen

button_click_DEL = Button(calculator, text="DEL", padx=10, pady=8, highlightbackground="#FFFF00", fg="black", command= button_click_delete)
button_click_DEL.grid(row=2, column=3)
button_click_DEL['font'] = myFont

button_click_AC = Button(calculator, text="AC", padx=14, pady=8, highlightbackground="yellow", fg="#000000", command = button_click_allClear)
button_click_AC.grid(row=2, column=4)
button_click_AC['font'] = myFont

# Buttons for arithmetic operators
button_click_divide = Button(calculator, text="÷", padx=25, pady=8, highlightbackground="green", fg="black", command=lambda: button_click_number('÷'))
button_click_divide.grid(row=4, column=3)
button_click_divide['font'] = myFont
button_click_multiple = Button(calculator, text="x", padx=25, pady=8, highlightbackground="#008000", fg="black", command=lambda: button_click_number('x'))
button_click_multiple.grid(row=4, column=4)
button_click_multiple['font'] = myFont

button_click_plus = Button(calculator, text="+", padx=25, pady=8, highlightbackground="green", fg="#000000", command=lambda: button_click_number('+'))
button_click_plus.grid(row=6, column=3)
button_click_plus['font'] = myFont
button_click_minus = Button(calculator, text="-", padx=25, pady=8, highlightbackground="green", fg="#000000", command=lambda: button_click_number('-'))
button_click_minus.grid(row=6, column=4)
button_click_minus['font'] = myFont

button_click_equally = Button(calculator, text="=", padx=68, pady=40, highlightbackground="blue", fg="#000000", command=button_click_equal)
button_click_equally.grid(row=8, column=3, rowspan=2, columnspan=2)
button_click_equally['font'] = myFont
calculator.mainloop()