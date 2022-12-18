

import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3

# 将麦克风识别到的.wav语音文件转成.txt文本文件
def speech_to_text():
    pass

# 基于chatterbot对.txt文本文件中的内容给出回复，转存成.txt文件
def smart_chatter():
    pass

# 基于pyttsx3，将.txt文本文件中的回复，转成.wav文件，并使用自定义的声音读出来
# 主要逻辑使用if else结构
def text2speech(goalStr):
    engine = pyttsx3.init()
    engine.setProperty('voice', "com.apple.speech.synthesis.voice.sin-ji")  # 需要重新设置成自己想要的语音包

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-40)
    engine.setProperty('volume', 0.7)
    engine.say(goalStr)
    engine.runAndWait()

if __name__ == '__main':
    strValue = "这是一个测试！"
    speak(strValue)