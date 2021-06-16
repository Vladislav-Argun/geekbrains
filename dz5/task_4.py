'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские
числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
translated = {'one' : 'один', 'two' : 'два', 'three' : 'три', 'four' : 'четыре', 'five' : 'пять', 'six' : 'шесть'}
with open('task_4.txt', 'r', encoding='utf-8') as file:
    with open('task_4_new.txt', 'w', encoding='utf-8') as file_2:
        for line in file:
            en, *num = line.split()
            ru = translated[en].lower()
            file_2.write(' '.join([ru] + num) + '\n')
"""
Посмотрите пожалуйста на код ниже, попробовал сделать голосового помошника
Если будет интерестно, можете запустить, предварительно установив все библиотеки
"""

# from gtts import gTTS
# from fuzzywuzzy import fuzz
# import pyttsx3
# import datetime
# import os
# import random
# import time
# import playsound
# import speech_recognition as sr
# speak_engine = pyttsx3.init()
# voices = speak_engine.getProperty('voices')
# speak_engine.setProperty('voice', voices[0].id)
# def speak(message):
#     print( message )
#     speak_engine.say( message )
#     speak_engine.runAndWait()
#     speak_engine.stop()

# def listen_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Скажите вашу команду: ")
#         audio = r.listen(source)
#     try:
#         our_speech = r.recognize_google(audio, language="ru")
#         print("Вы сказали: " + our_speech)
#         return our_speech
#     except sr.UnknownValueError:
#         return "ошибка"
#     except sr.RequestError:
#         return "ошибка"

# def do_this_command(message):
#     message = message.lower()
#     if "привет" in message:
#         speak("Привет друг!")
#     elif "пока" in message:
#         speak("Пока!")
#         exit()
#     elif "открой браузер" in message:
#         speak("Минутку...")
#     elif "cкажи" in message:
#         speak("Я не могу это сделать")
#     elif "ку-ку" in message:
#         speak("Ааааа? Чтоо? Гдее я? Чтоо я?")
#     elif "просыпайся" in message:
#         speak("А? Что? Где я? Что я?")
#     elif "кто ты" in message:
#         speak("Меня зовут Кеша, я ваш голосовой помошник.")
#         exit()
#     else:
#         speak("Команда не распознана!")

# if __name__ == '__main__':
#     while True:
#         command = listen_command()
#         do_this_command(command)