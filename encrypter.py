#Encrypter
import random
from random import randint

class Cipher():

	def get_entry(self):
		#get the user's password to encrypt
		self.inp_pass = input("Enter your password  ")

		#check
		while len(self.inp_pass) < 5:
			self.inp_pass = input("ERROR - password not long enough. Try again:  ")
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
		self.upper = 1
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
	print("\nYour new decrypted password is: ", encrypted)
	decrypted = new_pass.decrypt(encrypted)
	print("\nYour encrypted password is :", encrypted)
	print("Your decrypted password is :", decrypted, "\n")


















