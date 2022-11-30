from aip import AipSpeech
from pyaudio import PyAudio,paInt16
import requests,json,wave,time,pyttsx3
#百度AI，配置信息
APP_ID = ''#百度ai应用id
API_KEY = ''#百度ai应用的键值
SECRET_KEY = ''
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
#图灵机器，配置信息
TulingUrl='http://openapi.tuling123.com/openapi/api/v2'
turing_api_key = ""#图灵机器人api_key
 
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
#用户语音输入
def SaveVoice():
    pa=PyAudio()
    wf=wave.open(r'T.wav','wb')#打开wave文件
    wf.setnchannels(1)#配置声道数
    wf.setsampwidth(2)# 采样宽度2bytes
    wf.setframerate(16000)#采样率
    stream=pa.open(format=paInt16,channels=wf.getnchannels(),rate=wf.getframerate(),input=True,frames_per_buffer=1024)  #打开一个stream
    buff=[]#存储声音信息
    start=time.time()#开始运行时间戳
    print('用户说：')
    while time.time()<start+6:#录制6秒
        buff.append(stream.read(wf.getframerate()))
    stream.close()#关闭stream
    pa.terminate()
    wf.writeframes(b''.join(buff))
    wf.close()#关闭wave
 
#接受机器人响应
def RobotSpeakText(usersay="你好"):
    robot={
        "perception": {
            "inputText": {
                "text": usersay
            }
        },
        "userInfo": {
            "apiKey": turing_api_key ,
            "userId": 'Dudu'
         }
    }
    response=json.loads(requests.post(TulingUrl,None,robot,headers={'Content-Type':'charset=UTF-8'}).text)
    return str(response['results'][0]['values']['text'])
 
#语音发声
def RobotVoice(robotsay="我没听清，你在说一遍"):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-66)
    engine.say(robotsay)
    engine.runAndWait()
 
#主函数
def main():
    while True:
        try:
            SaveVoice()
            result = client.asr(get_file_content('T.wav'), 'wav', 16000, {'dev_pid': 1536})  # 识别本地文件
            usersay=result['result'][0]
            print(usersay)
            robotsay=RobotSpeakText(usersay)
            print('小嘟嘟说：')
            print(robotsay)
            RobotVoice(robotsay)
        except:#异常处理
            break
 
if __name__=='__main__':
    main()