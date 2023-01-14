from aiymakerkit import audio
import pyttsx3

import io
import sys
import argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

engine = pyttsx3.init()

text = "我是老铁，很高兴认识你！"
report_error = "对不起，我没听懂你说的话。"

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.setProperty('voice', 'zh')

def response(label, score):
    print('CALLBACK:', label, '==>', score)
    if label == 'laotie':
        engine.say(text)
        engine.runAndWait()
    else:
        engine.say(report_error)
        engine.runAndWait()
    return True

def main():
    audio.classify_audio(model_file=args.model, callback=response)

if __name__ == '__main__':
    main()
