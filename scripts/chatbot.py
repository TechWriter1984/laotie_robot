import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3
        
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def listen_and_convert():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        
        while True:
            text_to_speech("老铁正在听你说话哦！")
            try:
                audio = recognizer.listen(source)
                recognized_text = recognizer.recognize_google(audio, language='zh-CN')
                print("你说：", recognized_text)
                response = chatbot.get_response(recognized_text)
                print("老铁说：", response)
                text_to_speech(str(response))
            except sr.UnknownValueError:
                text_to_speech("对不起，我没听懂你说什么，你能再说一遍吗？")
            except sr.RequestError as e:
                print("语音识别错误：", e)
            
if __name__ == "__main__":
    # Set up the ChatterBot
    chatbot = ChatBot("老铁")
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.chinese")
    
    listen_and_convert()
