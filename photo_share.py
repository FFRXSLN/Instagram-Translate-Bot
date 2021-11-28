from words import all_tags , File_ , RemoveDelFiles
from botapi import Bot
from sharepost import InstaBot
import os

class AllOptions():
	def __init__(self,username,password):
		self.bot = Bot()
		self.crpost = InstaBot()
		self.files = []
		self.bot.login(username=username,password=password)

	def CreateForShare(self,count: int):
		self.crpost.Create_Words_With_Picture(name=f"eng.jpg",time=count)

	def Share(self):
		File_(self.files)
		while True:
			for i in self.files:
				self.bot.upload_photo(i,caption=f"Shared By [TRANSLATERBOT] {all_tags()}")
				self.files.remove(i)
				print(len(self.files))
				RemoveDelFiles()
				
# check this account https://www.instagram.com/dev.translate.py/
Login = AllOptions("username","password")
Login.CreateForShare(1) # Photo Count
Login.Share()