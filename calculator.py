import tkinter as tk
from tkinter import ttk

root = tk.Tk() #creates main window
root.title("Calculator")
root.geometry("450x400")
root.resizable(0,0) #disables resizing (width, height)
root.configure(bg='#FFE6F0')

#display and input field---------------------
display = tk.Entry (    #creates text input field
    root,
    font = ("Arial", 30),
    bg = ('#FFF5F5'),
    fg = ("#BE92C1"),
    borderwidth = 0,    #removes border
    justify  = 'right',  #aligns text to right side
    relief = 'flat',    #removes 3D
    highlightthickness = 0 #removes blue border
)

display.grid(
    row = 0,
    column = 0,
    columnspan = 4,
    padx = (75,20),
    pady = 20,    
    ipady = 25,    #increases height of input field
)

#setup ttk style for buttons------------------
style = ttk.Style()
style.theme_use("clam") #theme to clam which allows for more customization
style.configure(
    "Calc.TButton",
    bg = "#18EED9",
    fg = '#AF96FF',
    font = ("Arial", 22),
    borderwidth = 0,
    relief = 'flat'
)
style.map(
    "Calc.TButton",
    background = [("active", "#D8F1FF"),]
)

#buttons---------------

buttons = [
    ['7', '8', '9', '*'],
    ['4', '5', '6', '/'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for r, row in enumerate (buttons, start = 1): #makes buttons from list start at row 1
    for c, char in enumerate (row):
        button = ttk.Button(
            root,
            style = 'Calc.TButton',
            text = char,
            width = 4, #number of characters wide
        )
        button.grid(row=r, column=c, padx=5, pady=5)


root.mainloop() #keeps window open, should go at end of code