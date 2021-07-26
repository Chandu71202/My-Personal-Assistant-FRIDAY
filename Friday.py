# pip install SpeechRecognition   
import speech_recognition as sr
# pip install pyttsx3  if it doesn't work  pipwin install pyttsx3
import pyttsx3
# pip install pywhatkit
import pywhatkit
#pip install wikipedia
import wikipedia
#pip install googletrans
from googletrans import Translator
#pip install DateTime
from datetime import datetime
#pip install time
import time


"""
print("Note:  ")
print("       Please Ask your Question with the word 'Friday' . Orelse it thinks you are talking to somebody")
print("       To do any Google search Please use the word 'Google Search About' ")
print("       To play any songs or video's Please use the word 'Play'")
print("       To ask about Date or Time use 'date' for Date and 'time' for Time")
print("       To Translate anything Please use the word 'Translate'('I had set the translation value as Telugu(te) :)')")

"""
#print("Kindly please check the Readme file before executing this")

#You can add your own contact details
#save as "Name": 9414XXXXXX
phonebook={"Iron Man": 1433000,"Captain America":7017070170,"Thor":404404404,"Hulk":0000000,"Hawkeye":11111111,"Natasha":85208520}

def ProcessQuestion(question):
    #please include the sentence 'what are you doing' to ask what Friday is doing
    if 'what are you doing' in question:
        print("I am Waiting for your question....")
        talk("I am Waiting for your question....") 
        return True
    #please include the sentence 'how are you' if you want to ask Friday how is it
    elif 'how are you' in question:
        print("I'm doing good . Waiting for your question")
        talk("I'm doing good . Waiting for your question")
        return True
    #please include the word 'play' to play songs or video in youtube
    elif 'play' in question:
        talk(question)
        question=question.replace('play','')
        pywhatkit.playonyt(question)    
        return True
    #please include the word 'who is' to get the answer from wikipedia
    elif 'who is' in question:
        question=question.replace("who is"," ")
        print(wikipedia.summary(question,1))
        talk(wikipedia.summary(question,1))
        return True
    #please include the word 'time' to ask the time
    elif "time" in question:
        Time=datetime.today().time().strftime("%I:%M %p")
        print(Time)
        talk(Time)
    #please include the word 'date' to ask the date    
    elif "date" in question:
        date=datetime.today().date()
        print(date)
        talk(date)
        return True
    #please include the word 'translate' to translate from src="en"(english) to dest="te"(telugu)
    #you can change the src and dest lang values 
    #please refer this link  "https://media.geeksforgeeks.org/wp-content/uploads/20200430163105/google-trans-python.png"   for the code values of languages  
    elif "translate" in question:
        question=question.replace('translate',' ')
        t=Translator()
        result=t.translate(question,src="en",dest="te")
        print(result.text)
        talk(result.pronunciation)
        return True
    #just a silly thing 😂 if you want do try it with word 'I love you'  
    elif"I love you" in question:
        print("stop being silly boss")
        talk("stop being silly boss")
        return True
    #please use the word 'Google search about' to search in google
    elif "Google search about" in question:
        question=question.replace("Google search about"," ")
        pywhatkit.search(question)
        return True
    #to call anyone please include the word 'call' 
    #save the first letter of name with capital letter for better experience
    elif "call" in question:
        question=question.replace("call","")
        print(question)
        key=question[2:]
        if(key in phonebook.keys()):
            talk("Calling")
            print("Calling : ",key,"--",phonebook[key])
        else:
            print("You don't have that contact details")
            talk("You don't have that contact details")            
        return True  
    #if any of your commands won't work it asks to repeat the question
    #kindly refer the readme file :)
    else:
        print("Please Repeat your Question") 
        return True
def talk(answer):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    # to get female voice.If you need male set voices[1] as voices[0]  :)
    engine.setProperty('voice',voices[1].id) 
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-40)
    engine.say(answer)
    engine.runAndWait()


def getQuestion():
    r=sr.Recognizer()
    #getting input from the microphone
    with sr.Microphone() as source:
        print("Please Ask Your Question")
        audio=r.listen(source)

    try:
        #the command which you give must be a readable language preferably English
        question=r.recognize_google(audio)
        #without the word 'Friday' in the command Friday won't respond
        #else it thinks we are talking to someone behind which is done in else part
        if 'Friday' in question:
            question=question.replace("Friday","")
            print(question)
            return question
        #if you want to stop the execution anywhere just give command as 'stop' without the word 'Friday'  
        elif 'stop' in question:
            print("Bye. See you later. Have a nice day")
            talk("Bye. See you later. Have a nice day")
            return "not with me" 
        else:
            print("You are not talking to me carry on")
            talk("You are not talking to me carry on")
            return "not with me"
    # if the command is in not in any language or some disturbance sound it asks to repeat again
    except sr.UnknownValueError:
        print("Sorry I can't get You . Can you Please repeat again")
        talk("Sorry I can't get You . Can you Please repeat again")
        return("not with me")

canAskQuestion= True  
while canAskQuestion:
    question=getQuestion()
    if(question=="not with me"):
        canAskQuestion=False
    else:
        CanAskQuestion=ProcessQuestion(question)
        time.sleep(5)
