import openai
import pyttsx3
import os
import requests
import urllib3

def get_chat_response(prompt):
    # set up OpenAI API key and language
    openai.api_key = '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'
    openai.api_base = "https://api.openai.com/v1"
    openai.api_model = "text-davinci-002"
    openai.api_language = "zh"

    # disable SSL verification
    requests.packages.urllib3.disable_warnings()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # generate chat response from OpenAI
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # extract text from response
    text = response.choices[0].text.strip()
    print(f"ChatGPT: {text}")

    # initialize pyttsx3 engine
    engine = pyttsx3.init()

    # set voice property
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) # you can change the index to select a different voice

    # convert text to audio
    engine.save_to_file(text, 'response.wav')
    engine.runAndWait()

    # play audio file using Windows Media Player
    os.startfile('response.wav')


def main():
    # take user input for chat prompt
    prompt = input("Enter chat prompt (in Chinese): ")
    get_chat_response(prompt)


if __name__ == '__main__':
    main()
