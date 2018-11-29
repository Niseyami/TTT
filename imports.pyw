from lib import Login
loginMenu = Login.loginMenu
import tkinter as tk
import hashlib
import pickle as p
import os
loginwindow = tk.Tk()
loginMenu(loginwindow).pack(fill="both", expand=True)
loginwindow.mainloop()
