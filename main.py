from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from pocketsphinx import Pocketsphinx, Jsgf, FsgModel
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from gtts import gTTS
from playsound import playsound


import pyaudio
import sys
import os
import traceback
import speech_recognition as sr
import pyttsx3
import pygame


apikey = 'm7CZkDKOR5yUvcXxYcUHqGha2sz1z9VpXbEwwFkqpaD2'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/386adfb5-1855-43cf-ab3f-32a232286dae'

#authenticator = IAMAuthenticator(apikey)
#tts = TextToSpeechV1(authenticator=authenticator)
#tts.set_service_url(url)

bot = ChatBot("Nay", read_only=True)

speaker = pyttsx3.init()

"""
conversation = [
    "Olá",
    "Olá tudo bem?",
    "tudo sim e você?",
    "estou bem obrigado por perguntar",
    "e como vai o trabalho",
    "que legal ",
    "Muito bom!"
]
"""

trainer = ListTrainer(bot)
for _file in os.listdir('chats'):
    lines = open('chats/' + _file, 'r').readlines()

trainer.train(lines)


def cria_audio(audio):
    tts = gTTS(audio, lang='pt-BR')
    tts.save('bot.mp3')
    playsound('bot.mp3')

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        try:
            audio = r.listen(s)
            
            speech = r.recognize_google(audio, language='pt-BR')
            print('Você disse: ', speech)
            
            response = bot.get_response(speech)
            print('Nay: ', response)
            cria_audio(str(response))
        except:
            cria_audio('Desculpe Estou com falhas')
