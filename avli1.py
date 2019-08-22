#using seq2seq learning tensorflow and the encoder-decoder data is conv.txt
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from textblob import TextBlob
import pyttsx3
import speech_recognition as sr
import cvtest as c
import cv2

def listen():
 r = sr.Recognizer()
 with sr.Microphone() as source:
  print("Say something!")
  audio = r.listen(source)
 return(r.recognize_google(audio))
  
def write(thing):
 l = open('conv.txt','r').read()
 out = open('conv.txt','w')
 print(thing,file = out)
 print(l,file = out)
 out.close()

def sentiment(phrase):
 zen = TextBlob(phrase)
 o = zen.sentiment.polarity  
 t = zen.sentiment.subjectivity
 return([o,t])

def say(words): 
 engine = pyttsx3.init() 
 voices = engine.getProperty('voices')       
 engine.setProperty('voice', voices[1].id)
 engine.say(words)
 engine.runAndWait()
 engine.stop()

def train(chatbot):
 l1 = open('conv.txt','r').read()
 l2 = open('common_knowledge.txt','r').read()
 trainer = ChatterBotCorpusTrainer(chatbot)
 trainer.train(
    "chatterbot.corpus.english"
 )
 trainer = ListTrainer(chatbot)
 trainer.train(l1)
 trainer.train(l2)

def chat():
 sent = 0
 ysqh = False
 face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
 cap = cv2.VideoCapture(0) 
 l = open('conv.txt','r').read()
 chatbot = ChatBot("Ron Obvious")
 train(chatbot)
 last_input = None
 while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
  for (x1, y1, w1, h1) in faces:
   cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 2)  
#  cv2.imshow('frame',frame)
  if ysqh == False and c.smile(gray) >= 1 and sent > 0.7:
   print('you seem quite happy today')
   ysqh = True
  else:
   last_input = last_input
   x = input('go ahead: ')
   if x not in l:
    write(x)
    write(last_input)
    senti = sentiment(x)
    sent = senti[0]
    resp = chatbot.get_response(x)
    last_input = resp
    print(resp)
   else:  
    resp = chatbot.get_response(x)
    last_input = resp
    print(resp)
  if cv2.waitKey(20) & 0xFF == ord('q'):
   break
 cap.release()

def talk():
 sent = 0
 ysqh = False
 smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')
 face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
 cap = cv2.VideoCapture(0) 
 l = open('conv.txt','r').read()
 chatbot = ChatBot("Ron Obvious")
 train(chatbot)
 last_input = None
 while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
  for (x1, y1, w1, h1) in faces:
   roi_g = gray[y1:y1+h1,x1:x1+w1]
   roi_c = frame[y1:y1+h1,x1:x1+w1]
   smiles = smile_cascade.detectMultiScale(roi_g, 1.8, 20) 
  if ysqh == False and len(smiles) >= 1 and sent > 0.7:
   say('you seem quite happy today')
   ysqh = True
  elif ysqh == False and len(smiles) == 0 and sent < -0.7:
   say('you seem pretty sad today')
  else:
   last_input = last_input
   x = listen()
   senti = sentiment(x)
   sent = senti[0]
   if x not in l:
    resp = chatbot.get_response(x)
    say(resp)
    last_input = resp
    write(x)
    write(last_input)
   else:  
    resp = chatbot.get_response(x)
    last_input = resp
    say(resp)
  if cv2.waitKey(20) & 0xFF == ord('q'):
   break
