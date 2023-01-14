import pyttsx3
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.setProperty('voice', 'zh')

text1 = "你好，我是老铁，很高兴认识你"
text2 = "对不起，我没听懂你说什么"

def greeting():
    engine.say(text1)
    engine.runAndWait()

def dontknow():
    engine.say(text2)
    engine.runAndWait()

def main():
    pass
    #greeting()
    #dontknow()

#if __name__ == '__main__':
#    main()
