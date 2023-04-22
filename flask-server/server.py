import ctypes
import datetime
import json
import operator
import os
import random
import shutil
import smtplib
import subprocess
import time
import tkinter
import webbrowser
from urllib.request import urlopen

import feedparser
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import win32com.client as wincl
import winshell
import wolframalpha
from bs4 import BeautifulSoup
from clint.textui import progress
from ecapture import ecapture as ec
from flask import Flask
from gtts import gTTS
from twilio.rest import Client

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



app = Flask(__name__)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()
	engine.endLoop()
        
def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

# @app.route('/wishMe')
# def wishMe():
# 	hour = int(datetime.datetime.now().hour)
# 	if hour>= 0 and hour<12:
# 		speak("Good Morning !")

# 	elif hour>= 12 and hour<18:
# 		speak("Good Afternoon !")

# 	else:
# 		speak("Good Evening !")

# 	assname =("Pa ram")
# 	speak("I'm your personal assistant")
# 	speak(assname)
# 	return 'Wished!'

@app.route('/username')
def username():
    speak("What should i call you?")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    
    print("#####################".center(columns))
    print("Hey! hows it going, ", uname.center(columns))
    print("#####################".center(columns))
    
    speak("Hows it hanging?")

@app.route('/test')
def test():
	return 'test'

# def speak(audio):
# 	engine.say(audio)
# 	engine.runAndWait()

# def wishMe():
# 	hour = int(datetime.datetime.now().hour)
# 	if hour>= 0 and hour<12:
# 		speak("Good Morning !")

# 	elif hour>= 12 and hour<18:
# 		speak("Good Afternoon !")

# 	else:
# 		speak("Good Evening !")

# 	assname =("Pa ram")
# 	speak("I'm your personal assistant")
# 	speak(assname)
	

# def username():
# 	speak("What should i call you?")
# 	uname = takeCommand()
# 	speak("Welcome ")
# 	speak(uname)
# 	columns = shutil.get_terminal_size().columns
	
# 	print("#####################".center(columns))
# 	print("Hey! hows it going, ", uname.center(columns))
# 	print("#####################".center(columns))
	
# 	speak("Hows it hanging?")

# def takeCommand():
	
# 	r = sr.Recognizer()
	
# 	with sr.Microphone() as source:
		
# 		print("Listening...")
# 		r.pause_threshold = 1
# 		audio = r.listen(source)

# 	try:
# 		print("Recognizing...")
# 		query = r.recognize_google(audio, language ='en-in')
# 		print(f"User said: {query}\n")

# 	except Exception as e:
# 		print(e)
# 		print("Unable to Recognize your voice.")
# 		return "None"
	
# 	return query

# def sendEmail(to, content):
# 	server = smtplib.SMTP('smtp.gmail.com', 587)
# 	server.ehlo()
# 	server.starttls()
	
# 	# Enable low security in gmail
# 	server.login('your email id', 'your email password')
# 	server.sendmail('your email id', to, content)
# 	server.close()

# if __name__ == '__main__':
# 	clear = lambda: os.system('cls')
	
# 	# This Function will clean any
# 	# command before execution of this python file
# 	clear()
# 	wishMe()
# 	username()
	
# 	while True:
		
# 		query = takeCommand().lower()
		
# 		# All the commands said by user will be
# 		# stored here in 'query' and will be
# 		# converted to lower case for easily
# 		# recognition of command
# 		if 'wikipedia' in query:
# 			speak('Searching Wikipedia...')
# 			query = query.replace("wikipedia", "")
# 			results = wikipedia.summary(query, sentences = 3)
# 			speak("According to Wikipedia")
# 			print(results)
# 			speak(results)

# 		elif 'open youtube' in query:
# 			speak("Here you go to Youtube\n")
# 			webbrowser.open("youtube.com")

# 		elif 'open google' in query:
# 			speak("Here you go to Google\n")
# 			webbrowser.open("google.com")

# 		elif 'open stackoverflow' in query:
# 			speak("Here you go to Stack Over flow.Happy coding")
# 			webbrowser.open("stackoverflow.com")

# 		elif 'play music' in query or "play song" in query:
# 			speak("Here you go with music")

# 		elif 'the time' in query:
# 			strTime = datetime.datetime.now().strftime("% H:% M:% S")
# 			speak(f"Sir, the time is {strTime}")

# 		elif 'send a mail' in query:
# 			try:
# 				speak("What should I say?")
# 				content = takeCommand()
# 				speak("whome should i send")
# 				to = input()
# 				sendEmail(to, content)
# 				speak("Email has been sent !")
# 			except Exception as e:
# 				print(e)
# 				speak("I am not able to send this email")

# 		elif 'how are you' in query:
# 			speak("I've been worse")
# 			speak("How ya doin")

# 		elif 'fine' in query or "good" in query:
# 			speak("HELL YEAH!")

# 		elif "change my name to" in query:
# 			query = query.replace("change my name to", "")
# 			assname = query

# 		elif "change name" in query:
# 			speak("you're really gonna change my name? Aww maaan")
# 			assname = takeCommand()
# 			speak("This isnt a legal name change you know")

# 		elif "what's your name" in query or "What is your name" in query:
# 			speak("My friends call me")
# 			speak(assname)
# 			print("My friends call me", assname)

# 		elif 'exit' in query:
# 			speak("Thanks for giving me your time")
# 			exit()

# 		elif "who made you" in query or "who created you" in query:
# 			speak("I was made by Parth Shah.")
			
# 		elif 'joke' in query:
# 			speak(pyjokes.get_joke())
			
# 		elif "calculate" in query:
			
# 			app_id = "Wolframalpha api id"
# 			client = wolframalpha.Client(app_id)
# 			indx = query.lower().split().index('calculate')
# 			query = query.split()[indx + 1:]
# 			res = client.query(' '.join(query))
# 			answer = next(res.results).text
# 			print("The answer is " + answer)
# 			speak("The answer is " + answer)

# 		elif 'search' in query or 'play' in query:
			
# 			query = query.replace("search", "")
# 			query = query.replace("play", "")		
# 			webbrowser.open(query)


# 		elif 'change background' in query:
# 			ctypes.windll.user32.SystemParametersInfoW(20,
# 													0,
# 													"Location of wallpaper",
# 													0)
# 			speak("Background changed successfully")


# 		elif 'news' in query:
			
# 			try:
# 				jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
# 				data = json.load(jsonObj)
# 				i = 1
				
# 				speak('here are some top news from the times of india')
# 				print('''=============== TIMES OF INDIA ============'''+ '\n')
				
# 				for item in data['articles']:
					
# 					print(str(i) + '. ' + item['title'] + '\n')
# 					print(item['description'] + '\n')
# 					speak(str(i) + '. ' + item['title'] + '\n')
# 					i += 1
# 			except Exception as e:
				
# 				print(str(e))

		
# 		elif 'lock window' in query:
# 				speak("locking the device")
# 				ctypes.windll.user32.LockWorkStation()

# 		elif 'shutdown system' in query:
# 				speak("Hold On a Sec ! Your system is on its way to shut down")
# 				subprocess.call('shutdown / p /f')
				
# 		elif 'empty recycle bin' in query:
# 			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
# 			speak("Recycle Bin Recycled")

# 		elif "don't listen" in query or "stop listening" in query:
# 			speak("how long should i stop listening for?")
# 			a = int(takeCommand())
# 			time.sleep(a)
# 			print(a)

# 		elif "where is" in query:
# 			query = query.replace("where is", "")
# 			location = query
# 			speak("User asked to Locate")
# 			speak(location)
# 			webbrowser.open("https://www.google.nl / maps / place/" + location + "")

# 		elif "camera" in query or "take a photo" in query:
# 			ec.capture(0, "Param Camera ", "img.jpg")

# 		elif "restart" in query:
# 			subprocess.call(["shutdown", "/r"])
			
# 		elif "hibernate" in query or "sleep" in query:
# 			speak("Hibernating")
# 			subprocess.call("shutdown / h")

# 		elif "log off" in query or "sign out" in query:
# 			speak("Make sure all the application are closed before sign-out")
# 			time.sleep(5)
# 			subprocess.call(["shutdown", "/l"])

# 		elif "write a note" in query:
# 			speak("What should i write, sir")
# 			note = takeCommand()
# 			file = open('jarvis.txt', 'w')
# 			speak("Sir, Should i include date and time")
# 			snfm = takeCommand()
# 			if 'yes' in snfm or 'sure' in snfm:
# 				strTime = datetime.datetime.now().strftime("% H:% M:% S")
# 				file.write(strTime)
# 				file.write(" :- ")
# 				file.write(note)
# 			else:
# 				file.write(note)
		
# 		elif "show note" in query:
# 			speak("Showing Notes")
# 			file = open("jarvis.txt", "r")
# 			print(file.read())
# 			speak(file.read(6))

# 		elif "update assistant" in query:
# 			speak("After downloading file please replace this file with the downloaded one")
# 			url = '# url after uploading file'
# 			r = requests.get(url, stream = True)
			
# 			with open("Voice.py", "wb") as Pypdf:
				
# 				total_length = int(r.headers.get('content-length'))
				
# 				for ch in progress.bar(r.iter_content(chunk_size = 2391975),
# 									expected_size =(total_length / 1024) + 1):
# 					if ch:
# 					    Pypdf.write(ch)
					
# 		# NPPR9-FWDCX-D2C8J-H872K-2YT43
# 		elif "Param" in query:
			
# 			wishMe()
# 			speak("Param here, how can I help?")
# 			speak(assname)

# 		elif "weather" in query:
			
# 			# Google Open weather website
# 			# to get API of Open weather
# 			api_key = "Api key"
# 			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
# 			speak(" City name ")
# 			print("City name : ")
# 			city_name = takeCommand()
# 			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
# 			response = requests.get(complete_url)
# 			x = response.json()
			
# 			if x["code"] != "404":
# 				y = x["main"]
# 				current_temperature = y["temp"]
# 				current_pressure = y["pressure"]
# 				current_humidiy = y["humidity"]
# 				z = x["weather"]
# 				weather_description = z[0]["description"]
# 				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			
# 			else:
# 				speak(" City Not Found ")

# 		elif "wikipedia" in query:
# 			webbrowser.open("wikipedia.com")

# 		elif "Good Morning" in query:
# 			speak("A warm" +query)
# 			speak("How are you")
# 			speak(assname)

# 		elif "how are you" in query:
# 			speak("I'm alive i guess")

# 		elif "i love you" in query:
# 			speak("oh god not the abington meta ")

# 		elif "what is" in query or "who is" in query:
			
# 			# Use the same API key
# 			# that we have generated earlier
# 			client = wolframalpha.Client("API_ID")
# 			res = client.query(query)
			
# 			try:
# 				print (next(res.results).text)
# 				speak (next(res.results).text)
# 			except StopIteration:
# 				print ("No results")

# 		# elif "" in query:
# 			# Command go here
# 			# For adding more commands


if __name__ == '__main__':
    app.run(debug=True)