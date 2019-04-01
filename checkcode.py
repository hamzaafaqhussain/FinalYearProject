import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
Entry, mainloop, StringVar
import tkinter as tk


root = tk.Tk()
w = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
##w.grid(column=0, row=1, columnspan=2, rowspan=2)
w.grid(column=0, row=1, columnspan=2, rowspan=2, sticky="ew")
tk.Label(root,text="column 0").grid(row=0,column=0)
tk.Label(root,text="column 1").grid(row=0,column=1)

root.mainloop()
