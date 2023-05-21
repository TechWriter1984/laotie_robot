# -*- coding: utf-8 -*-
# @Time    :   2023/05/14 22:50:37
# @FileName:   chatter.py
# @Author  :   TechWriter1984
# @E-mail  :   oopswow@126.com

import speech_recognition as sr
import pyttsx3
import aiy.voice.tts
from aiy.board import Board
from aiy.leds import Leds
import requests

# Define the ChatGPT endpoint
GPT_ENDPOINT = "http://api.openai.com/v1/engines/davinci-codex/completions"

# Define the parameters for the ChatGPT request
GPT_PARAMS = {
    "prompt": "",
    "max_tokens": 50,
    "temperature": 0.7,
    "stop": "\n",
}

# Define the function to send a request to ChatGPT and get the response
def get_gpt_response(prompt):
    # Set the prompt for the ChatGPT request
    GPT_PARAMS["prompt"] = prompt

    # Send the request to ChatGPT
    response = requests.post(GPT_ENDPOINT, headers={"Authorization": "Bearer INSERT_YOUR_API_KEY_HERE"}, json=GPT_PARAMS)

    # Get the response from ChatGPT
    response_json = response.json()

    # Get the chat response from the JSON
    chat_response = response_json["choices"][0]["text"]

    # Return the chat response
    return chat_response

# Define the function to convert text to speech
def text_to_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set the properties for the engine
    engine.setProperty("rate", 150)

    # Convert the text to speech
    engine.say(text)
    engine.runAndWait()

# Define the function to start the voice chat
def start_voice_chat():
    # Initialize the SpeechRecognition recognizer
    recognizer = sr.Recognizer()

    # Set the microphone as the audio source
    microphone = sr.Microphone()

    # Start the chat loop
    while True:
        try:
            # Listen for the user's voice command
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            # Use Google API to recognize the user's voice command
            text = recognizer.recognize_google(audio, language="zh-CN")

            # Print the user's voice command
            print("User said: " + text)

            # Use ChatGPT to get the chat response
            chat_response = get_gpt_response(text)

            # Print the chat response
            print("Chat response: " + chat_response)

            # Convert the chat response to speech
            text_to_speech(chat_response)

        except sr.UnknownValueError:
            # If the user's voice command cannot be recognized, print an error message
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            # If the Google API request fails, print an error message
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

