import tkinter as tk
from tkinter import messagebox
import pyautogui as pg
import time

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

# Open Windows Calculator via CLI
def openCalculator():
    pg.hotkey('winleft', 'r')
    pg.typewrite('calc')
    pg.press('enter')
    # Wait for the Calculator: 2 Seconds
    time.sleep(2)
    

# Close Calculator
def closeCalculator():
    pg.press('escape')
    pg.hotkey('alt', 'f4')

# Addition
def Addition():
    openCalculator()
    pg.press('escape',)
    pg.press('7')
    pg.press('+')
    pg.press('3')
    pg.press('enter')
    time.sleep(2)
    closeCalculator()

# Subtraction
def Subtraction():
    openCalculator()
    pg.press('escape')
    pg.press('7')
    pg.press('-')
    pg.press('3')
    pg.press('enter')
    time.sleep(2)
    closeCalculator()

# Multiplication
def Multiplication():
    openCalculator()
    pg.press('escape')
    pg.press('7')
    pg.press('*')
    pg.press('3')
    pg.press('enter')
    time.sleep(2)
    closeCalculator()

# Division
def Division():
    openCalculator()
    pg.press('escape')
    pg.press('7')
    pg.press('/')
    pg.press('3')
    pg.press('enter')
    time.sleep(2)
    closeCalculator()

top = tk.Tk()
top.title('AutoCalc')
top.geometry('300x300')

A = tk.Button(top, text ="Addition", command = Addition)
A.pack(ipadx=10, ipady=10, pady=10)

S = tk.Button(top, text ="Subtraction", command = Subtraction)
S.pack(ipadx=10, ipady=10, pady=10)

M = tk.Button(top, text ="Multiplication", command = Multiplication)
M.pack(ipadx=10, ipady=10, pady=10)

D = tk.Button(top, text ="Division", command = Division)
D.pack(ipadx=10, ipady=10, pady=10)

top.mainloop()