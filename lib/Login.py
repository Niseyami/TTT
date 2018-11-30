##These are the login functions of a Tic Tac Toe/Naughts and Crosses game made in python
##Made in Python version 3.7.0
##GUI is made with tkinter, as shown below
##Made for a Year 9 IT class taken at GVGS
##Do not edit unless you know what your doing, as this is a crutial part of the program

#Imports
import tkinter as tk
import hashlib
import pickle as p
import os

#Main class
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
        self.title = tk.Label(self, text="PyTTT Login", font="TkFixedFont 14", bg="white", anchor="n")
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
        except FileExistsError:
            self.UsrExists = tk.Label(self, text="User already exists", bg="red")
            self.UsrExists.grid(column=1, row=8, sticky="s")
        passvarUTF8 = passvar.encode('utf-8')
        passvarHashed = hashlib.sha3_512(passvarUTF8).hexdigest()
        currentaccount = str(usrvar)
        del usrvar
        del passvar
        del passvarUTF8
        initWins = 0
        initLoses = 0
        usrVariables = [currentaccount, passvarHashed, initWins, initLoses]
        #DataLocation = ("/usr/%s/AccountDetails.dat" % currentaccount)
        #pickle.dump("", DataLocation, 0)
        #with open(DataLocation, "wb+") as data:
        #    pickle.dump(usrVariables, data, 0)
        #file = pickle.load(DataLocation, "rb+")
        #print(file)
        for widget in self.winfo_children():
            widget.destroy()
        self.maintext = tk.Label(self, text="Account successfully registered", bg="white", font="TkFixedFont 14")
        self.subtext = tk.Label(self, text="You may now close this window", bg="white", font="TkFixedFont 12")
        self.maintext.grid(column=0, row=0)
        self.subtext.grid(column=0, row=1)
        
    def login(self):
        print('placeholder')



loginwindow = tk.Tk()
loginMenu(loginwindow).pack(fill="both", expand=True)
loginwindow.mainloop()
