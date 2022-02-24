from words import get_word , save_words , is_exists , FuckTheString
from googletrans import Translator
import os,time,cv2,random
from instabot import Bot

class InstaBot(object):
	def CreatePicture(self,word,name=None,main=None):
		img = cv2.imread(main,cv2.IMREAD_UNCHANGED)

		WORD = Translator().translate(word,dest='tr').text
		wordnorm = FuckTheString(WORD.lower())

		wordtr = f"( {wordnorm} )"

		textsize = cv2.getTextSize(word, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 4)[0]
		textsize1 = cv2.getTextSize(wordtr, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 4)[0]

		cv2.putText(img, word, (int((img.shape[1] - textsize[0]) / 2), int((img.shape[0] + textsize[1]) / 2)-50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (131,255, 0), 6)
		cv2.putText(img, wordtr, (int((img.shape[1] - textsize1[0]) / 2), int((img.shape[0] + textsize1[1]) / 2)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,255, 255), 6)
		
		if word in wordnorm:
			pass
		else:
			if os.path.exists(name) == True:
				name = f"new{random.randrange(1000,100000000000)}" + name
			print(f"---\n{name} : {word}\n---")
			cv2.imwrite(name,img)
			#cv2.imshow(name,img)
			#cv2.waitKey(0)
		save_words(word)


	def Create_Words_With_Picture(self,name,time : int):
		global is_exists,get_word
		MAIN_photos = ["main1.png"]

		if time != 0:
			i = 0
			while True:
				main=f"{os.getcwd()}\\{random.choice(MAIN_photos)}"
				word = get_word()

				if is_exists(word) != True:
					if i == time:
						break
					else:
						i+=1

					try:
						self.CreatePicture(word,f"{i}{name}",main)
					except Exception as hata:
						print(str(word) + " : " + str(hata))
