#Encrypter
import random
from random import randint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

class Database():

	def __init__(self):
		#database stuff
		pass


class Screen():

	bgCol = "#%02x%02x%02x"%(160,239,194)
	
	def __init__(self):
		#make default window
	    self.root = Tk()
	    self.root.geometry('480x500+200+100')
	    self.root.title('Password Encrypter')
	    self.root.resizable(0,0)
	    self.root.configure(background=self.bgCol)
	    self.note = ttk.Notebook(self.root, width=480, height=500)
	    self.passEncTab = Frame(self.note, bg=self.bgCol)
	    self.note.add(self.passEncTab, text='Encrypt Password')
	    self.note.pack()

	    self.password = StringVar()
	    self.encPassword = StringVar()

	    self.ttlLbl = Label(self.passEncTab, bg=self.bgCol, text="Enter your password below:", font=("Helvetica",25)).grid(row=0,column=0,pady=(50,0))
	    self.passEntry = Entry(self.passEncTab, highlightbackground=self.bgCol, textvariable=self.password).grid(row=1,column=0,pady=(10,0))
	    self.encryptButton = Button(self.passEncTab, text='ENCRYPT', command=self.get_entry, font=("Helvetica",28)).grid(row=3,column=0,pady=(10,0),columnspan=3)

	    self.origLabel = Label(self.passEncTab, text="Your Password", font=("Helvetica",20)).grid(row=4,column=0,pady=(20,0))
	    self.newLabel = Label(self.passEncTab, text="Encrypted Password", font=("Helvetica",20)).grid(row=6,column=0,pady=(10,0))

	    self.origPassLbl = Label(self.passEncTab, textvariable=self.password, font=("Helvetica",18)).grid(row=5,column=0,pady=(10,0))
	    self.encPassLbl = Label(self.passEncTab, textvariable=self.encPassword, font=("Helvetica",18)).grid(row=7,column=0,pady=(10,0))

	    



class Cipher(Screen):

	def get_entry(self):
		#get the user's password to encrypt
		print(self.password.get())

		#check
		if len(self.password.get()) < 5:
			self.errorMessage = messagebox.showwarning(title='Error',message='Password not long enough - must be 5 characters or more.')
		else:
			#take input
			self.orig_pass_dict = {}
			self.inc = 0
			for let in self.inp_pass:
				self.orig_pass_dict[self.inc] = let
				self.inc += 1

			return self.inp_pass


	def encrypt(self, password):
		#securely encrypt the password
		self.upper_alph = []
		self.lower_alph = []
		self.enc_pass = ""
		self.new_pass_dict = {}

		#append alphabet
		for u in range (65,91):
			self.upper_alph.append(chr(u))
			self.lower_alph.append(chr(32 + u))

		#create encrypted key
		for i in range(1,len(password)+1):
			self.rand_val = random.randint(1,2)
			if self.rand_val == 1:
				self.enc_pass += self.upper_alph[random.randint(1,24)]
			else:
				self.enc_pass += self.lower_alph[random.randint(1,24)]

		for dec in range(0,len(self.enc_pass)):
			self.new_pass_dict[dec] = self.enc_pass[dec]

		return self.enc_pass


	def decrypt(self, password):
		#decrypt the password
		while True:
			try:
				opt = int(input("Want to decrpyt your password? (1=yes,2=no)"))
				break
			except ValueError:
				print("Oops, try again. \n")
		
		if opt == 1:
			#decrypt
			self.dec_pass = ""
			for key in self.new_pass_dict:
				self.dec_pass += self.orig_pass_dict[key]

			return self.dec_pass
		else:
			quit()	


if __name__ == "__main__":
	new_pass = Cipher()
	password = new_pass.get_entry()
	encrypted = new_pass.encrypt(password)
	print("\nYour new encrypted password is: ", encrypted)
	decrypted = new_pass.decrypt(encrypted)
	print("\nYour encrypted password is :", encrypted)
	print("Your decrypted password is :", decrypted, "\n")


















