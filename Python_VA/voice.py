import tkinter as tk
import speech_recognition as sr
import pyttsx3
import webbrowser
import pygame
import datetime
import threading

window = tk.Tk()
window.title("Voice Assistant")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

pygame.mixer.init()

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def voice_assistant():
    try:
        with sr.Microphone() as source:
            print("Listening for a command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("Recognizing...")

        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "sing a song" in command:
            speak("Sure, I'll sing a song for you.")
            song_file = "C:\\Users\\91912\\Desktop\\Python_VA\\Music\\Kumkumala-Nuvve.mp3"
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")
        elif "tell me a joke" in command:
            speak("Why did the computer catch a cold? Because it had too many windows!")
        elif "who are you" in command:
            speak("I am a Python-based voice assistant. How can I help you today?")
        elif "thank you" in command:
            speak("You're welcome!")
        # Add more commands and responses as needed...
        else:
            speak("I'm sorry, I didn't understand that. Please type your command.")
            type_command()

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that. Please type your command.")
        type_command()
    except sr.RequestError:
        speak("Sorry, I couldn't request results; check your network connection.")
        type_command()


def type_command():
    command = input("Type your command: ").lower()
    if "sing a song" in command:
        speak("Sure, I'll sing a song for you.")
        song_file = "path_to_your_song.mp3" 
        play_audio(song_file)
    else:
        speak("I'm sorry, I didn't understand that.")

assistant_button = tk.Button(window, text="Start Voice Assistant", command=voice_assistant)
assistant_button.pack()

window.mainloop()
