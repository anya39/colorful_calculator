#setup--------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk

root = tk.Tk() #creates main window
root.title("Calculator")
root.geometry("450x400")
root.resizable(0,0) #disables resizing (width, height)
root.configure(bg='#FFE6F0')

#creates display and input field--------------------------------------------------------------------
display = tk.Entry (    #creates text input field
    root,
    font = ("Times New Roman", 35),
    bg = ("#FFFFFF"),
    fg = ("#BE92C1"),
    borderwidth = 0,    #removes border
    justify  = 'right',  #aligns text to right side
    relief = 'flat',    #removes 3D
    highlightthickness = 0 #removes border
)

display.grid(
    row = 0,
    column = 0,
    columnspan = 4,
    padx = (75,20),
    pady = 20,    
    ipady = 25,    #increases height of input field
)

#creates button functions--------------------------------------------------------------------
def add_to_display(value):
    display.insert(tk.END, value) 

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "error")

#setup ttk style for buttons--------------------------------------------------------------------
style = ttk.Style()
style.theme_use("clam") #theme to clam which allows for more customization
style.configure(
    "Calc.TButton",
    font = ("Times New Roman", 25),
    borderwidth = 0,
    relief = 'flat'
)
style.map(
    "Calc.TButton",
    background = [("active", "#FBFFD8"),]
)

#creates buttons--------------------------------------------------------------------
buttons = [
    ['7', '8', '9', '*'],
    ['4', '5', '6', '/'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for r, row in enumerate (buttons, start = 1): #makes buttons from list start at row 1
    for c, char in enumerate (row):
        if char == 'C':
            cmd = clear_display
        elif char == '=':
            cmd = calculate
        else:
            cmd = lambda ch=char: add_to_display(ch)
        button = ttk.Button(
            root,
            style = 'Calc.TButton',
            text = char,
            width = 4, #number of characters wide
            command = cmd
        )
        button.grid(row=r, column=c, padx=5, pady=5)


root.mainloop() #keeps window open, should go at end of code