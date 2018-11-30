##PyTTT by A Person
##Made from Python Version 3.7.0
##Do not edit unless you know what your are doing

#Imports
import tkinter as tk
from PIL import ImageTk, Image

#My modules to import
from lib.StartMenu import startMenu
from lib.Login import loginMenu


currentUser = ''


global startwindow
startwindow = tk.Tk()
startMenu(startwindow).pack(fill="both", expand=True)
startwindow.mainloop()
