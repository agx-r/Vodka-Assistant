import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import socket
import platform


def get_pc_info():
	system = platform.system()
	release = platform.release()
	version = platform.version()
	machine = platform.machine()
	processor = platform.processor()

	information = f"System: {system}\n" \
				  f"Release: {release}\n" \
				  f"Version: {version}\n" \
				  f"Machine: {machine}\n" \
				  f"Processor: {processor}"

	return information


def get_network_info():
	"""Returns information about the network."""
	hostname = socket.gethostname()
	ip_address = socket.gethostbyname(hostname)
	return f"Хост: {hostname}\nАйпи: {ip_address}"


# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Function to speak out the assistant's response
def speak(text):
	engine.say(text)
	print(f"Vodka assistant: {text}")
	engine.runAndWait()


# Function to listen to the user's voice input
def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='ru')
		print(f"User: {query}")
		return query.lower()
	except sr.UnknownValueError:
		print("I didn't understand that.")
		return "Что?"
	except sr.RequestError:
		print("Sorry, I'm not available right now.")
		return "Распознавание речи недоступно. Ошибка отправки запроса."


# Function to handle user commands
def process_command(command):
	if 'время' in command:
		current_time = datetime.datetime.now().strftime("%H:%M")
		speak(f"Сейчас {current_time}")
	elif 'поиск' in command:
		search_query = command.replace('search ', '').replace('for ', '')
		speak(f"Поиск {search_query}")
		webbrowser.open(f"https://www.google.com/search?q={search_query}")
	elif 'network' in command:
		speak(get_network_info())
	elif 'информация о железе' in command:
		speak(get_pc_info())
	elif 'википедия' in command:
		search_query = command.replace('википедия ', '')
		if search_query == '':
			speak(f"ЭРРОР")
			return
		speak(f"Поиск в вики по квери запросу {search_query}")
		try:
			wikipedia.set_lang("ru")
			content = wikipedia.summary(search_query, sentences=3)
			speak(f"Вот что нашлось: {content}")
		except Exception as e:
			speak(f"Ошибка. Проверьте консоль.")
			print(e)
	elif 'мой ip' in command:
		speak(get_network_info().split("\n")[-1])
	elif 'умри' in command:
		speak("Умираю")
		exit()
	else:
		print(command)
		speak(command)


# Main program loop
if __name__ == '__main__':
	speak("Асистент запущен")
	while True:
		command = listen()
		process_command(command)
