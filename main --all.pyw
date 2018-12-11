#print(ad) || total
#print(ad[0]) || Name
#print(ad[1]) || Passhashed sha3_512
#print(ad[2]) || Wins
#print(ad[3]) || Losses
#print(ad[4]) || Draws
#print(ad[5]) || Account type || 0/Standard | 1/SuperUser | 2/Admin | 3/Debug
#print(ad[6]) || Profile Picture Location

#Imports
import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import ImageTk, Image
import hashlib
import pickle
import os
import time

#Start menu
class startMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        startwindow.title("PyTTT")
        self.config(bg="white")
        self.logo = ImageTk.PhotoImage(Image.open("assests/Logo.pgm"))
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
        try:
            profilewindow.destroy()
        except:
            pass
        #game.singlePlayer()
        
    def playMulti(self):
        startwindow.destroy()
        try:
            profilewindow.destroy()
        except:
            pass
        #game.multiPlayer()
        
    def profile(self):
        if currentUser != "":
            global profilewindow
            profilewindow = tk.Toplevel()
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
        self.loginButton = tk.Button(self, text="Login", font="TkFixedFont 12", bg="white", command=self.login)
        self.registerButton = tk.Button(self, text="register", font="TkFixedFont 12", bg="white", command=self.register)
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
        if len(self.userInputForm.get()) == 0 or self.userInputForm.get() == " ":
            self.usernameWarning = tk.Label(self, text="Username cannot be empty", bg="red")
            self.usernameWarning.grid(column=1, row=6, sticky="s")
        if len(self.passwordInputForm.get()) == 0 or self.passwordInputForm.get() == " ":
            self.passwordWarning = tk.Label(self, text="Password cannot be empty", bg="red")
            self.passwordWarning.grid(column=1, row=7, sticky="s")
        if len(self.userInputForm.get()) > 0 and self.userInputForm.get() != " ":
            if len(self.passwordInputForm.get()) > 0 and self.passwordInputForm.get() != " ":
                self.initializeaccount() 

    def initializeaccount(self):
        usrvar = self.userInputForm.get()
        passvar = self.passwordInputForm.get()
        usrDirectory = (f"./usr/{usrvar}")
        try:
            os.mkdir(usrDirectory)
            passvarHashed = hashlib.sha3_512(passvar.encode("utf-8")).hexdigest()
            global currentUser
            currentUser = str(usrvar)
            del usrvar
            del passvar
            initWins = 0
            initLoses = 0
            initDraws = 0
            initAccountType = 0
            initProfilePicture = "./assets/Blank-Profile-Picture.pgm"
            usrVariables = [currentUser, passvarHashed, initWins, initLoses, initDraws, initAccountType, initProfilePicture]
            DataLocation = (f"./usr/{currentUser}/AccountDetails.dat")
            with open(DataLocation, "wb+") as data:
                pickle.dump(usrVariables, data, 0)
                data.close()
            for widget in self.winfo_children():
                widget.destroy()
            self.maintext = tk.Label(self, text="Account successfully registered", bg="white", font="TkFixedFont 14")
            self.subtext = tk.Label(self, text="You may now close this window", bg="white", font="TkFixedFont 12")
            global Wins
            global Loses
            global Draws
            global profilePicture
            global accountType
            Wins = initWins
            Loses = initLoses
            Draws = initDraws
            accountType = initAccountType
            profilePicture = initProfilePicture
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
        DataLocation = (f"./usr/{usrvar}")
        if len(usrvar) > 0:
            try:
                os.mkdir(DataLocation)
                os.rmdir(DataLocation)
                self.usrNotExists = tk.Label(self, text="User does not exists", bg="red")
                self.usrNotExists.grid(column=1, row=6, sticky="s")
            except FileExistsError:
                for widget in self.winfo_children():
                    widget.destroy()                  
                self.config(bg="white")
                self.title = tk.Label(self, text=f"Welcome {usrvar}", font="TkFixedFont 14", bg="white", anchor="n")
                self.subtitle = tk.Label(self, text="Enter your password:", font="TkFixedFont 12", bg="white", anchor="n")
                self.passwordInputForm = tk.Entry(self, show="*")
                self.passwordInputForm.config(highlightbackground="white", highlightthickness=0)
                self.credentialsSubmitButton = tk.Button(self, text="Login", bg="white", font="TkFixedFont 12", command=self.loginpasswordsubmit)
                self.title.grid(column=1, row=1, sticky="n")
                self.subtitle.grid(column=1, row=2, sticky="n")
                self.passwordInputForm.grid(column=1, row=3, padx=20, sticky="e")
                self.credentialsSubmitButton.grid(column=1, row=4, sticky="s")
        else:
            self.usrBlank = tk.Label(self, text="Username cannot be Blank", bg="red")
            self.usrBlank.grid(column=1, row=5, sticky="s")
            
    def loginpasswordsubmit(self):
        passvar = self.passwordInputForm.get()
        DataLocation = (f"./usr/{usrvar}/AccountDetails.dat")
        with open(DataLocation, "rb+") as UsrData:
            logonDetails = pickle.load(UsrData)
            UsrData.close()
        if hashlib.sha3_512(passvar.encode("utf-8")).hexdigest() == logonDetails[1]:
            global currentUser
            currentUser = usrvar
            for widget in self.winfo_children():
                widget.destroy()
            global Wins
            global Loses
            global Draws
            global accountType
            global profilePicture
            Wins = logonDetails[2]
            Loses = logonDetails[3]
            Draws = logonDetails[4]
            accountType = logonDetails[5]
            profilePicture = logonDetails[6]
            self.config(bg="white")
            self.title = tk.Label(self, text=f"Welcome {currentUser}", font="TkFixedFont 14", bg="white", anchor="n")
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
        
#Profile class
class profileMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(bg="white")
        profilewindow.title(f"{currentUser}'s Profile")
        self.title = tk.Label(self, text=f"Welcome {currentUser}", font="TkFixedFont 18 bold", bg="white")
        self.logo = ImageTk.PhotoImage(Image.open(profilePicture))
        self.logoLabel = tk.Label(self, image=self.logo, bg="white")
        self.statsDisplay = tk.Label(self, text=f"Wins: {Wins}\nLoses: {Loses}\nDraws: {Draws}", font="TkFixedFont 15 bold", bg="white")
        self.editProfileButton = tk.Button(self, text="Edit Profile", bg="white", font="TkFixedFont 12", command=self.editprofile)    
        self.exitProfileButton = tk.Button(self, text="Exit", bg="white", font="TkFixedFont 12", command=profilewindow.destroy)
        self.title.grid(column=0, row=0, columnspan=2)
        self.logoLabel.grid(column=0, row=1, sticky="w")
        self.statsDisplay.grid(column=1, row=1, sticky="w")
        self.editProfileButton.grid(column=0, row=2, sticky="news")
        self.exitProfileButton.grid(column=1, row=2, sticky="news")
        
    def editprofile(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.title = tk.Label(self, text="Change account details", bg="white", font="TkFixedFont 15 bold")
        self.changePictureButton = tk.Button(self, text="Change profile picture", bg="white", command=self.changeprofilepicture)
        self.changeUsernameButton = tk.Button(self, text="Change account username", bg="white", command=self.changeaccountusername)
        self.changePasswordButton = tk.Button(self, text="Change account password", bg="white", command=self.changeaccountpassword)
        self.title.grid(column=0, row=0)
        self.changePictureButton.grid(column=0, row=1, sticky="news")
        self.changeUsernameButton.grid(column=0, row=2, sticky="news")
        self.changePasswordButton.grid(column=0, row=3, sticky="news")

    def changeprofilepicture(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.title = tk.Label(self, text="Change profile picture", bg="white", font="TkFixedFont 15 bold")
        self.pathEntry = tk.Entry(self, width=60)
        self.selectPathButton = tk.Button(self, text="Select image", bg="white", command=self.loadprofilepicturepath)
        self.next = tk.Button(self, text="Next", bg="white", command=self.confirmprofilepicture)
        self.back = tk.Button(self, text="Back", bg="white", command=self.__init__)
        self.title.grid(column=0, row=0, columnspan=2)
        self.pathEntry.grid(column=0, row=1, columnspan=2)
        self.absDefaultPath = os.path.abspath(profilePicture)
        self.pathEntry.insert(0, self.absDefaultPath)
        self.selectPathButton.grid(column=1, row=2, sticky="e")
        self.next.grid(column=1, row=3, sticky="news")
        self.back.grid(column=0, row=3, sticky="news")

    def loadprofilepicturepath(self):
        filename = filedialog.askopenfilename(filetypes = (("Jpeg files", "*.jpg"), ("Png files", "*.png")))
        self.pathEntry.delete(0, tk.END)
        self.pathEntry.insert(0, filename)

    def confirmprofilepicture(self):
        try:
            self.profilePicturePreDownsample = Image.open(self.pathEntry.get())
            basewidth = 180
            wpercent = (basewidth/float(self.profilePicturePreDownsample.size[0]))
            hsize = int((float(self.profilePicturePreDownsample.size[1])*float(wpercent)))
            self.profilePictureDownsample = self.profilePicturePreDownsample.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
            self.profilePictureDownsample.save(f"./usr/{currentUser}/profilePicture.gif")
            global profilePicture
            profilePicture = f"./usr/{currentUser}/profilePicture.gif"
        except IOError:
            self.notImageFormat = tk.Label(self, text="That is not a valid image", bg="red")
            self.notImageFormat.grid(column=0, row=4, columnspan=2)
                            #########################################################################################
    def changeaccountusername(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.title = tk.Label(self, text="Change your username", bg="white", font="TkFixedFont 16 bold")
        self.passwordSubtitle = tk.Label(self, text="Current password:", bg="white")
        self.passwordInputForm = tk.Entry(self, show="*")
        self.passwordConfirmSubtitle = tk.Label(self, text="Confirm password:", bg="white")
        self.passwordConfirmForm = tk.Entry(self, show="*")
        self.passwordSubmitButton = tk.Button(self, text="Submit", bg="white", command=self.changeuser)
        self.title.grid(column=0, row=0, sticky="news", columnspan=2)
        self.passwordSubtitle.grid(column=0, row=1)
        self.passwordInputForm.grid(column=1, row=1)
        self.passwordConfirmSubtitle.grid(column=0, row=2)
        self.passwordConfirmForm.grid(column=1, row=2)
        self.passwordSubmitButton.grid(column=0, row=3, sticky="news", columnspan=2)

    def changeuser(self):
        if self.passwordInputForm.get() == self.passwordConfirmForm.get():
            DataLocation = (f"./usr/{currentUser}/AccountDetails.dat")
            with open(DataLocation, "rb+") as UsrData:
                Details = pickle.load(UsrData)
                UsrData.close()
            if Details[1] == hashlib.sha3_512(self.passwordInputForm.get().encode("utf-8")).hexdigest() and Details[1] == hashlib.sha3_512(self.passwordConfirmForm.get().encode("utf-8")).hexdigest():
                for widget in self.winfo_children():
                    widget.destroy()
                self.title = tk.Label(self, text="Change your username", bg="white", font="TkFixedFont 16 bold")
                self.currentUserSubtitle = tk.Label(self, text="Current username:", bg="white")
                self.currentUserForm = tk.Entry(self)
                self.newUserSubtitle = tk.Label(self, text="New username:", bg="white")
                self.newUserForm = tk.Entry(self)
                self.usernameChangeConfirm = tk.Button(self, text="Confirm Changes", bg="white", command=self.confirmusernamechange)
                self.title.grid(column=0, row=0, columnspan=2)
                self.currentUserSubtitle.grid(column=0, row=1)
                self.currentUserForm.grid(column=1, row=1)
                self.newUserSubtitle.grid(column=0, row=2)
                self.newUserForm.grid(column=1, row=2)
                self.usernameChangeConfirm.grid(column=0, row=3, columnspan=2)
            else:
                self.passIncorrect = tk.Label(self, text="Password is incorrect", bg="red")
                self.passIncorrect.grid(column=0, row=4, sticky="news", columnspan=2)
        else:
            self.passNotMatch = tk.Label(self, text="Passwords do not match", bg="red")
            self.passNotMatch.grid(column=0, row=5, sticky="news", columnspan=2)

    def confirmusernamechange(self):
        if currentUser == self.currentUserForm.get():
            if self.newUserForm.get() != " " and len(self.newUserForm.get()) > 0:
                DataLocation = (f"./usr/{currentUser}/AccountDetails.dat")
                with open(DataLocation, "rb+") as UsrData:
                    Details = pickle.load(UsrData)
                    UsrData.close()
                newUser = self.newUserForm.get()
                passvarHashed = Details[1]
                if Details[6] != "./assests/Blank-Profile-Picture.pgm":
                    profileUser = self.newUserForm.get()
                    profilePicture = f"./usr/{profileUser}/Profile Picture.gif"
                usrVariables = [newUser, passvarHashed, Wins, Loses, Draws, accountType, profilePicture]
                with open(DataLocation, "wb+") as data:
                    pickle.dump(usrVariables, data, 0)
                    data.close()
                os.rename(f"./usr/{currentUser}", f"./usr/{self.newUserForm.get()}")
                global OldUsername
                OldUsername = currentUser
                self.inituserchange()
            else:
                self.newUserInvalid = tk.Label(self, text="New username cannot be empty", bg="red")
                self.newUserInvalid.grid(column=0, row=4, sticky="news", columnspan=2)
        else:
            self.currentUserIncorrect = tk.Label(self, text="Current username is incorrect", bg="red")
            self.currentUserIncorrect.grid(column=0, row=5, sticky="news", columnspan=2)

    def inituserchange(self):
        global currentUser
        currentUser = self.newUserForm.get()
        for widget in self.winfo_children():
            widget.destroy()
        self.title = tk.Label(self, text="Username Successfully changed", bg="white", font="TkFixedFont 15 bold")
        self.subtitle = tk.Label(self, text=f"From {OldUsername} --> {currentUser}", bg="white", font="TkFixedFont 12 bold")
        #self.profileWarning = tk.Label(self, text="Due to limitations, your profile picture has been changed to the default picture", bg="white")
        #self.profileWarningFix = tk.Label(self, text="Please change it again to access your profile profile picture", bg="white")
        self.quitButton = tk.Button(self, text="Exit", bg="white", command=profilewindow.destroy)
        self.title.grid(column=0, row=0)
        self.subtitle.grid(column=0, row=1)
        #self.profileWarning.grid(column=0, row=2)
        #self.profileWarningFix.grid(column=0, row=3)
        self.quitButton.grid(column=0, row=4)
    
    def changeaccountpassword(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.title = tk.Label(self, text="Change your password", bg="white", font="TkFixedFont 16 bold")
        self.passwordSubtitle = tk.Label(self, text="Current password:", bg="white")
        self.passwordConfirmSubtitle = tk.Label(self, text="Confirm password:", bg="white")
        self.passwordInputForm = tk.Entry(self, show="*")
        self.passwordConfirmForm = tk.Entry(self, show="*")
        self.passwordSubmitButton = tk.Button(self, text="Submit", bg="white", command=self.changepassword)
        self.title.grid(column=0, row=0, sticky="news", columnspan=2)
        self.passwordSubtitle.grid(column=0, row=1)
        self.passwordInputForm.grid(column=1, row=1)
        self.passwordConfirmSubtitle.grid(column=0, row=2)
        self.passwordConfirmForm.grid(column=1, row=2)
        self.passwordSubmitButton.grid(column=0, row=3, sticky="news", columnspan=2)

    def changepassword(self):
        if self.passwordInputForm.get() == self.passwordConfirmForm.get():
            DataLocation = (f"./usr/{currentUser}/AccountDetails.dat")
            with open(DataLocation, "rb+") as UsrData:
                Details = pickle.load(UsrData)
                UsrData.close()
            if Details[1] == hashlib.sha3_512(self.passwordInputForm.get().encode("utf-8")).hexdigest() and Details[1] == hashlib.sha3_512(self.passwordConfirmForm.get().encode("utf-8")).hexdigest():
                for widget in self.winfo_children():
                    widget.destroy()
                self.title = tk.Label(self, text="Change your password", bg="white", font="TkFixedFont 16 bold")
                self.newPasswordSubtitle = tk.Label(self, text="New password:", bg="white")
                self.newPasswordForm = tk.Entry(self, show="*")
                self.passwordConfirmSubtitle = tk.Label(self, text="Confirm password:", bg="white")
                self.passwordConfirmForm = tk.Entry(self, show="*")
                self.passwordChangeConfirm = tk.Button(self, text="Confirm Changes", bg="white", command=self.confirmpasswordchange)
                self.title.grid(column=0, row=0, columnspan=2)
                self.newPasswordSubtitle.grid(column=0, row=1)
                self.newPasswordForm.grid(column=1, row=1)
                self.passwordConfirmSubtitle.grid(column=0, row=2)
                self.passwordConfirmForm.grid(column=1, row=2)
                self.passwordChangeConfirm.grid(column=0, row=3, columnspan=2)
            else:
                self.passIncorrect = tk.Label(self, text="Password is incorrect", bg="red")
                self.passIncorrect.grid(column=0, row=4, sticky="news", columnspan=2)
        else:
            self.passNotMatch = tk.Label(self, text="Passwords do not match", bg="red")
            self.passNotMatch.grid(column=0, row=5, sticky="news", columnspan=2)

    def confirmpasswordchange(self):
        if self.newPasswordForm.get() == self.passwordConfirmForm.get():
            if self.newPasswordForm.get() != " " and len(self.newPasswordForm.get()) > 0:
                DataLocation = (f"./usr/{currentUser}/AccountDetails.dat")
                with open(DataLocation, "rb+") as UsrData:
                    Details = pickle.load(UsrData)
                    UsrData.close()
                passvarHashed = hashlib.sha3_512(self.newPasswordForm.get().encode("utf-8")).hexdigest()
                usrVariables = [currentUser, passvarHashed, Wins, Loses, Draws, accountType, profilePicture]
                with open(DataLocation, "wb+") as data:
                    pickle.dump(usrVariables, data, 0)
                    data.close()
                for widget in self.winfo_children():
                    widget.destroy()
                self.title = tk.Label(self, text="Password successfuly changed", bg="white", font="TkFixedFont 16 bold")
                self.closeButton = tk.Button(self, text="Close", bg="white", command=profilewindow.destroy)
                self.title.grid(column=0, row=0)
                self.closeButton.grid(column=0, row=1)
            else:
                newUserInvalid = tk.Label(self, text="New password cannot be empty", bg="red")
                newUserInvalid.grid(column=0, row=4, sticky="news", columnspan=2)
        else:
            self.newPassNotMatch = tk.Label(self, text="New passwords do not match", bg="red")
            self.newPassNotMatch.grid(column=0, row=5, sticky="news", columnspan=2)

currentUser = ""
startwindow = tk.Tk()
startMenu(startwindow).pack(fill="both", expand=True)
startwindow.mainloop()
