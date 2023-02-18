# -*- coding: utf-8 -*-
# @Time    :   2023/01/14 15:41:03
# @FileName:   chatbot.py
# @Author  :   TechWriter1984
# @E-mail  :   oopswow@126.com

import pyttsx3
import sys
import io
from random import choice
from datetime import datetime

class Chatbot():
    
    def __init__(self):

        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice', 'zh')

    def greeting(self):
        text1 = "你好，我是老铁。很高兴认识你！"
        text3 = "哎~！老铁在呢！"
        text4 = "喊我干嘛啊？是不是想我了啊？"
        list_greetings = [text1, text3, text4]
        self.engine.say(choice(list_greetings))
        self.engine.runAndWait()

    def dontknow(self):
        text2 = "对不起，我没听懂你说什么，你能再说一次吗？"        
        self.engine.say(text2)
        self.engine.runAndWait()

    def current_time(self):
        now = datetime.now()
        format_time = now.strftime("现在是%H点%M分")
        self.engine.say(format_time)
        self.engine.runAndWait()

# def main():
#     chatbot = Chatbot()
#     chatbot.greeting()
#     chatbot.dontknow()
#     chatbot.current_time()

# if __name__ == '__main__':
#     main()
