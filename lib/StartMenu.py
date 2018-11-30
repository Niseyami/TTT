##The start menus of a Tic Tac Toe/Naughts and Crosses game made in python
##Made in Python version 3.7.0
##GUI is made with tkinter, as shown below
##Made for a Year 9 IT class taken at GVGS
##Do not edit unless you know what your doing, as this is a crutial part of the program

#Imports
import tkinter as tk
from PIL import ImageTk, Image

if __name__ == "__main__":
    currentUser = ''

#Start menu
class startMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        startwindow.title("PyTTT")
        self.config(bg="white")
        try:
            self.logo = ImageTk.PhotoImage(Image.open("./lib/Logo.pgm"))
        except FileNotFoundError:
            self.logo = ImageTk.PhotoImage(Image.open("Logo.pgm"))
        logoLabel = tk.Label(self, image=self.logo, bg="white")
        self.promptUpper = tk.Label(self, text="PyTTT", anchor="c", font="TkFixedFont 18 bold", bg="white")
        self.buttonSingle = tk.Button(self, text="Single Player", font="TkFixedFont 12", bg="white", command = self.playSingle)
        self.buttonMulti = tk.Button(self, text="Two Players", font="TkFixedFont 12", bg="white", command = self.playMulti)
        self.buttonProfile = tk.Button(self, text="Profile", font="TkFixedFont 12", bg="white", command = self.profile)
        self.buttonExit = tk.Button(self, text="Exit", font="TkFixedFont 12", bg="white", command = self.sysExit)
        self.promptLower = tk.Label(self, text="Made with Python 3.7 by Sasith De Abrew", bg="white", anchor="s")
        self.promptUpper.pack(side="top", fill="x", expand=1)
        logoLabel.pack(side="right", anchor="e", padx=10)
        self.buttonSingle.pack(side="top", anchor="w", expand=1, padx=10)
        self.buttonMulti.pack(side="top", anchor="w", expand=1, padx=10)
        self.buttonProfile.pack(side="top", anchor="w", expand=1, padx=10)
        self.buttonExit.pack(side="top", anchor="w", expand=1, padx=10)
        self.promptLower.pack(side="bottom", fill="x", anchor="s")

    def playSingle(self):
        startwindow.destroy()
        game.singlePlayer()
        
    def playMulti(self):
        startwindow.destroy()
        game.multiPlayer()
        
    def profile(self):
        if currentUser != '':
            profile.curretUser()
        else:
            global loginwindow
            loginwindow = tk.Tk()
            loginMenu(loginwindow).pack(fill="both", expand=True)
            loginwindow.mainloop()
        
    def sysExit(self):
        startwindow.destroy()
        raise SystemExit

startwindow = tk.Tk()
startMenu(startwindow).pack(fill="both", expand=True)
startwindow.mainloop()

