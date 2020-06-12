import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import pass1


#voice selection for jarvis
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#voices is a list of voices on your computer
engine.setProperty('voice',voices[1].id)


#speak function will take string input and speak
def speak(audio):
	engine.say(audio)
	engine.runAndWait()


#wishMe() function will greet you whenever you run this script
def wishMe():
	hour = int(datetime.datetime.now().hour)
	
	if hour>=0 and hour<12:
		speak("good morning Sir")

	elif hour>=12 and hour<18:
		speak("good afternoon sir")
	
	else:
		speak("Good Evening sir")

	speak("I am jarvis sir. Tell me how can i help you?")


#jarvis will take your voice command and convert into string
def takeCommand():
	#it takes microphone input from user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		
	try:
		print("Recognizing...")
		query = r.recognize_google(audio,language='en-in')
		print(f"User said; {query}\n")

	except Exception as e:
		print(e)
		print("Say That Again Please...")
		return "None"

	return query

#jarvis will send email and please make sure to make your gmail account less secure.
def sendEmail(to,content):
	e = pass1.getEmail()
	p = pass1.getPass()
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login(e,p)
	server.sendmail(e,to,content)
	server.close()

if __name__ == "__main__":
	wishMe()
	while True:
		query = takeCommand().lower()
		#Logic for executing tasks based on query
		
		if 'according to wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace('according to wikipedia','')
			results = wikipedia.summary(query,sentences=2)
			speak("According to wikipedia")
			print(results)
			speak(results)
		elif 'open youtube' in query:
			speak('opening youtube..')
			webbrowser.open("youtube.com")

		elif 'according to google' in query:
			speak('opening google..')
			query = query.replace('according to google','')
			webbrowser.open("http://google.com/#q="+query,new=2)
		
		elif 'open facebook' in query:
			speak('opening facebook..')
			webbrowser.open("facebook.com")

		elif 'open github' in query:
			speak('opening github..')
			webbrowser.open("github.com")

		elif 'play music' in query:
			music_dir = "C:\\Users\\hites\\OneDrive\\Desktop\\music"
			songs = os.listdir(music_dir)
			n = len(songs)
			index = random.randint(0,n)
			os.startfile(os.path.join(music_dir,songs[index]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			print(strTime)
			speak(f"Sir,the time is {strTime}")

		elif 'open editor' in query:
			speak('opening sublime text editor..')
			path = "C:\\Users\\hites\\OneDrive\\Desktop\\Sublime Text 3\\sublime_text.exe"
			os.startfile(path)
			
		elif 'send email' in query:
			try:
				speak("What should i say?")
				content = takeCommand()
				to = "youremail@gmail.com"
				sendEmail(to,content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry Hitesh sir,I am not able to send this email")
			

		elif 'who are you' in query:
			speak('I am jarvis sir')
		
		elif 'goodbye' in query:
			speak('goodbye sir')
			exit()
		
			
