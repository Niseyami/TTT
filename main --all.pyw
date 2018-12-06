#Imports
import tkinter as tk
from PIL import ImageTk, Image
import hashlib
import pickle
import os
import time

#Defining vars
currentUser = ''

#Start menu
class startMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        startwindow.title("PyTTT")
        self.config(bg="white")
        self.logo = ImageTk.PhotoImage(Image.open("lib/Logo.pgm"))
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
            global profilewindow
            profilewindow = tk.Tk()
            profileMenu(profilewindow).pack(fill="both", expand=True)
            profilewindow.mainloop()
        else:
            global loginwindow
            loginwindow = tk.Tk()
            loginMenu(loginwindow).pack(fill="both", expand=True)
            loginwindow.mainloop()
            
    def sysExit(self):
        startwindow.destroy()
        raise SystemExit

#Login Class
class loginMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        loginwindow.title("PyTTT Login")
        self.config(bg="white")
        self.title = tk.Label(self, text="PyTTT Login", font="TkFixedFont 14", bg="white", anchor="n")
        self.subtitle = tk.Label(self, text="Please register or log in", font="TkFixedFont 12", bg="white", anchor="n")
        self.loginButton = tk.Button(self, text="Login", font="TkFixedFont 12", command=self.login)
        self.registerButton = tk.Button(self, text="register", font="TkFixedFont 12", command=self.register)
        self.title.pack(side="top", anchor="n")
        self.subtitle.pack(side="top", anchor="n")
        self.loginButton.pack(side="left", padx=20, pady=10)
        self.registerButton.pack(side="right", padx=20, pady=10)

    def register(self):
        loginwindow.title("PyTTT Register")
        for widget in self.winfo_children():
            widget.destroy()
        self.config(bg="white")
        self.title = tk.Label(self, text="PyTTT Register", font="TkFixedFont 14", bg="white", anchor="n")
        self.subtitle = tk.Label(self, text="Enter a username and password", font="TkFixedFont 12", bg="white", anchor="n")
        self.userSubtitle = tk.Label(self, text="Username:", font="TkFixedFont 10", bg="white")
        self.userInputForm = tk.Entry(self)
        self.userInputForm.config(highlightbackground="white", highlightthickness=0)
        self.passwordSubtitle = tk.Label(self, text="Password:", font="TkFixedFont 10", bg="white")
        self.passwordInputForm = tk.Entry(self, show="*")
        self.passwordInputForm.config(highlightbackground="white", highlightthickness=0)
        self.credentialsSubmitButton = tk.Button(self, text="Register", bg="white", font="TkFixedFont 12", command=self.registeraccount)
        self.title.grid(column=1, row=1, sticky="n")
        self.subtitle.grid(column=1, row=2, sticky="n")
        self.userSubtitle.grid(column=1, row=3, sticky="w")
        self.userInputForm.grid(column=1, row=3, padx=20, sticky="e")
        self.passwordSubtitle.grid(column=1, row=4, sticky="w")
        self.passwordInputForm.grid(column=1, row=4, padx=20, sticky="e")
        self.credentialsSubmitButton.grid(column=1, row=5, sticky="s")

    def registeraccount(self):
        if len(self.userInputForm.get()) == 0 or self.userInputForm.get() == ' ':
            self.usernameWarning = tk.Label(self, text="Username cannot be empty", bg="red")
            self.usernameWarning.grid(column=1, row=6, sticky="s")
        if len(self.passwordInputForm.get()) == 0 or self.passwordInputForm.get() == ' ':
            self.passwordWarning = tk.Label(self, text="Password cannot be empty", bg="red")
            self.passwordWarning.grid(column=1, row=7, sticky="s")
        if len(self.userInputForm.get()) > 0 and self.userInputForm.get() != ' ':
            if len(self.passwordInputForm.get()) > 0 and self.passwordInputForm.get() != ' ':
                self.initializeaccount() 

    def initializeaccount(self):
        usrvar = self.userInputForm.get()
        passvar = self.passwordInputForm.get()
        usrDirectory = ("./usr/%s" % usrvar)
        try:
            os.mkdir(usrDirectory)
            passvarHashed = hashlib.sha3_512(passvar.encode('utf-8')).hexdigest()
            currentUser = str(usrvar)
            del usrvar
            del passvar
            initWins = 0
            initLoses = 0
            initAccountType = 0
            initProfilePicture = "./lib/Blank-Profile-Picture.pgm"
            usrVariables = [currentUser, passvarHashed, initWins, initLoses, initAccountType, initProfilePicture]
            DataLocation = ("./usr/%s/AccountDetails.dat" % currentUser)
            with open(DataLocation, "wb+") as data:
                pickle.dump(usrVariables, data, 0)
                data.close()
            for widget in self.winfo_children():
                widget.destroy()
            self.maintext = tk.Label(self, text="Account successfully registered", bg="white", font="TkFixedFont 14")
            self.subtext = tk.Label(self, text="You may now close this window", bg="white", font="TkFixedFont 12")
            global Wins
            global Loses
            Wins = initWins
            Loses = initLoses
            self.closeWindowButton = tk.Button(self, text="Close", bg="white", font="TkFixedFont 12", command=loginwindow.destroy)
            self.maintext.grid(column=0, row=0)
            self.subtext.grid(column=0, row=1)
            self.closeWindowButton.grid(column=0, row=2)
        except FileExistsError:
            self.UsrExists = tk.Label(self, text="User already exists", bg="red")
            self.UsrExists.grid(column=1, row=8, sticky="s")
        
    def login(self):
        loginwindow.title("PyTTT Login")
        for widget in self.winfo_children():
            widget.destroy()
        self.config(bg="white")
        self.title = tk.Label(self, text="PyTTT Login", font="TkFixedFont 14", bg="white", anchor="n")
        self.subtitle = tk.Label(self, text="Enter your username:", font="TkFixedFont 12", bg="white", anchor="n")
        self.userInputForm = tk.Entry(self)
        self.userInputForm.config(highlightbackground="white", highlightthickness=0)
        self.credentialsSubmitButton = tk.Button(self, text="Login", bg="white", font="TkFixedFont 12", command=self.loginusersubmit)
        self.title.grid(column=1, row=1, sticky="n")
        self.subtitle.grid(column=1, row=2, sticky="n")
        self.userInputForm.grid(column=1, row=3, padx=20, sticky="e")
        self.credentialsSubmitButton.grid(column=1, row=4, sticky="s")

    def loginusersubmit(self):
        global usrvar
        usrvar = self.userInputForm.get()
        DataLocation = ("./usr/%s" % usrvar)
        try:
            os.mkdir(DataLocation)
            os.rmdir(DataLocation)
            self.usrNotExists = tk.Label(self, text="User does not exists", bg="red")
            self.usrNotExists.grid(column=1, row=5, sticky="s")
        except FileExistsError:
            DataLocation = ("./usr/%s/AccountDetails.dat" % usrvar)
            for widget in self.winfo_children():
                widget.destroy()                  
            self.config(bg="white")
            self.title = tk.Label(self, text="Welcome %s" % usrvar, font="TkFixedFont 14", bg="white", anchor="n")
            self.subtitle = tk.Label(self, text="Enter your password:", font="TkFixedFont 12", bg="white", anchor="n")
            self.passwordInputForm = tk.Entry(self, show="*")
            self.passwordInputForm.config(highlightbackground="white", highlightthickness=0)
            self.credentialsSubmitButton = tk.Button(self, text="Login", bg="white", font="TkFixedFont 12", command=self.loginpasswordsubmit)
            self.title.grid(column=1, row=1, sticky="n")
            self.subtitle.grid(column=1, row=2, sticky="n")
            self.passwordInputForm.grid(column=1, row=3, padx=20, sticky="e")
            self.credentialsSubmitButton.grid(column=1, row=4, sticky="s")
            
    def loginpasswordsubmit(self):
        passvar = self.passwordInputForm.get()
        DataLocation = ("./usr/%s/AccountDetails.dat" % usrvar)
        with open(DataLocation, "rb+") as UsrData:
            logonDetails = pickle.load(UsrData)
            UsrData.close()
        if hashlib.sha3_512(passvar.encode('utf-8')).hexdigest() == logonDetails[1]:
            global currentUser
            currentUser = usrvar
            for widget in self.winfo_children():
                widget.destroy()
            global Wins
            global Loses
            global accountType
            global ProfilePicture
            Wins = logonDetails[2]
            Loses = logonDetails[3]
            accountType = logonDetails[4]
            profilePicture = logonDetails[5]
            self.config(bg="white")
            self.title = tk.Label(self, text="Welcome %s" % currentUser, font="TkFixedFont 14", bg="white", anchor="n")
            self.subtitle = tk.Label(self, text="Your Infomation has been accepted", font="TkFixedFont 12", bg="white", anchor="n")
            self.subsubtitle = tk.Label(self, text="You may close this window", font="TkFixedFont 12", bg="white", anchor="n")
            self.closeWindowButton = tk.Button(self, text="Close", bg="white", font="TkFixedFont 12", command=loginwindow.destroy)
            self.title.grid(column=1, row=1, sticky="n")
            self.subtitle.grid(column=1, row=2, sticky="n")
            self.subsubtitle.grid(column=1, row=3, padx=20, sticky="e")
            self.closeWindowButton.grid(column=1, row=4, sticky="s")
        else:
            self.passNotValid = tk.Label(self, text="Password is not valid", bg="red")
            self.passNotValid.grid(column=1, row=5, sticky="s")
        
                #print(ad) || total
                #print(ad[0]) || Name
                #print(ad[1]) || Passhashed sha3_512
                #print(ad[2]) || Wins
                #print(ad[3]) || Losses
                #print(ad[4]) || Account type || 0/Standard | 1/SuperUser | 2/Admin | 3/Debug
                #print(ad[5]) || Profile Picture Location

#Profile class
class profileMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(bg="white")
        profilewindow.title("%s's Account" % currentUser)
        #self.logo = ImageTk.PhotoImage(Image.open(profilePicture))
        self.title = tk.Label(self, text="Welcome %s" % currentUser, anchor="c", font="TkFixedFont 18 bold", bg="white")
        self.subtitle = tk.Label(self, text="Made with Python 3.7 by Sasith De Abrew", bg="white", anchor="s")
        self.title.pack(side="top", fill="x", expand=1)
        self.subtitle.pack(side="bottom", fill="x", anchor="s")
        
startwindow = tk.Tk()
startMenu(startwindow).pack(fill="both", expand=True)
startwindow.mainloop()
