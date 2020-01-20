from gtts import gTTS
import os
import sys
import wikipedia
import speech_recognition as sr
import re
import webbrowser
r= sr.Recognizer()
while True:
	with sr.Microphone() as source:
		print("SAY SOMETHING");
		audio = r.listen(source)
		print("GOT IT")
		t=r.recognize_google(audio)
		if t=='exit' or 'shut up' in t or 'dont bark' in t: 
			exit();
		elif t=='shutdown my computer':
			sys.exit();
		elif 'open' in t:
			reg_ex = re.search('open (.+)', t)
			if reg_ex:
				domain = reg_ex.group(1)
				print(domain)
				url = 'https://www.' + domain
				webbrowser.open(url)
			else:
				pass
		elif 'more about' in t:
			reg_ex=re.search('more about (.+)', t)
			if reg_ex:
				domain = reg_ex.group(1)
				print(domain)
				file = "file.mp3"
				n=wikipedia.page(domain).content
				ttts = gTTS(n,'en')
				print(n)
				ttts.save(file);
				os.system("mpg123 " + file)
		else:
			print(t)
			s = wikipedia.summary(t)
			file = "file.mp3"
			tts = gTTS(s, 'en')
			print(s);
			tts.save(file)
			os.system("mpg123 " + file)
