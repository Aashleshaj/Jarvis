import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
	
def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<=12:
		speak("good morning!")
		
	elif hour>12 and hour<=18:
		speak("good afternoon!")
		
	else:
		speak("good night!")
	
	speak("hello am braina how may i help you")
	
def sendEmail(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('aiassistanct111@gmail.com','seemajadhav123')
	server.sendmail('aiassistanct111@gmail.com',to,content)
	server.close()		
				
			
def takecommands():
	i=1
	print("To exit the program type any number except 1")
	while(True):
		
		user=input("enter your wish:")
		if 'open google' in user:
			webbrowser.open("google.com")
			
		elif 'open youtube' in user:
			webbrowser.open("youtube.com")
			
		elif 'open stackoverflow' in user:
			webbrowser.open("stackoverflow.com")
				
		elif 'open facebook' in user:
			webbrowser.open("facebook.com")
		elif 'time' in user:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(strTime)
			print(strTime)
			
		elif 'open notepad' in user:
			codepath="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
			os.startfile(codepath)
			
		elif 'open cmd' in user:
			codepath="C:\\WINDOWS\\system32\\cmd"
			os.startfile(codepath)
			
		elif 'wikipedia' in user:
			speak('searching wikipedia......')
			user=user.replace("wikipedia","")
			results=wikipedia.summary(user,sentences=2)
			speak("according to wikipedia")
			speak(results)
			print(results)
		
		elif 'play music' in user:
			music_dir="C:\\Users\OWN\Music\songs"
			songs=os.listdir(music_dir)
			print(songs)
			x=random.choice(songs)
			print(x)		
			os.startfile(os.path.join(music_dir,songs[2]))
		
		elif 'send email' in user:
			try:
				speak("to whom you whant to send mail")
				to=input("to whom you whant to send mail: ")
				speak("enter your mail")
				content=input("enter your mail: ")
				sendEmail(to,content)
				speak("Email has been send")
				print("Email has been send")
			except Exception as a:
				print(a)
				speak("sorry can't send your email ")
				
		else:
			speak("good bye!")
			exit()
			
	

	
	
        

	
if __name__== "__main__":
	wishMe()
	takecommands()
		
		