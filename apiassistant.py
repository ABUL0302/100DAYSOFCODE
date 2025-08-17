import pyttsx3
import google.generativeai as genai

engine= pyttsx3.init()


enter=input('enter your query: ')
model=genai.GenerativeModel('gemini-2.0-flash')
client=genai.configure(api_key='API_KEY')
response=model.generate_content(enter)
print(response.text)
engine.say(response.text)
engine.runAndWait()

