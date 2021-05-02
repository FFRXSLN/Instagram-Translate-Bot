import random , os
from all_words import word

words = []
extag = ["grammar","verbs","newwords","onlinelessons","howtospeak","ingilizcekonus","eğitim","ielts","yabancıdil","learnenglish","englishforlife","ingilizceçeviri","ingilizcekitap","otelcilik","ingilizceogren","hafızateknikleri","turizim","toefl","yökdil","ingilizcekelime","vocabulary","ingilizceöğreniyorum","ingilizcekelimeler",'ingilizcedersi  ', 'ingilizcekursu ', 'ingilteredekiturkler ', 'ingilizceöğreniyorum ', 'ingilizceşarkılar ', 'ingilizcedeyimler ', 'ingilizcekalıplar ', 'ingilizcesözler ', 'yds ', 'ydt ', 'yökdil ', 'ydskelimeler ', 'ydtkelime ', 'yds2020 ', 'ingilisdili ', 'akıcıingilizce ', 'ingilizcepratik ', 'turkish ', 'turkishlanguage ', 'ingilizcekelime ', 'ingilizce']
turkish = {	
	"ı" : "i",
	"ğ" : "g",
	"ö" : "o",
	"ç" : "c",
	"ü" : "u",
	"ş" : "s",
	"İ" : "i"
}

for i in word.split("\n"):
	words.append(i)

delfiles = []
passed=0

def get_word():
	global words,passed
	_w_ = words[passed]
	#print(f"{passed} ->{_w_}")
	passed+=1
	return _w_
	
def is_exists(word):
	with open("words.txt") as f:
		for i in f.readlines():
			if word in i:
				return True
				
def save_words(word):
	with open("words.txt","a") as words:
		words.writelines(str(word) + "\n")

def FuckTheString(string):
	global turkish
	sp = ""
	for x in string:
		for y in turkish:
			if y in x:
				x = x.replace(y,str(turkish[y]))
		sp += x
	return sp

def all_tags():
	bitis = 0
	alltagused = ""
	usefultags = []

	while True:
		if bitis == 20:
			break
		else:
			normtag = f"#{random.choice(extag)}"
			if normtag not in usefultags:
				usefultags.append(normtag)
				bitis+=1
			else:
				#print(normtag)
				pass
	
	for a in usefultags:
		alltagused += a + " "

	return alltagused

def File_(file : list):
	global files

	for i in os.listdir(os.getcwd()):
		if i.endswith("jpg"):
			file.append(i)

def RemoveDelFiles():
	global delfiles
	delfiles.clear()

	for i in os.listdir(os.getcwd()):
		if i.endswith("REMOVE_ME"):
			delfiles.append(i)

	for i in delfiles:
		os.remove(i)