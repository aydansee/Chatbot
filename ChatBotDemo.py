import pyttsx3
import speech_recognition as sr
from tkinter import *

root=Tk()
def send():
    send="You => " +e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Bot => Hi")
    elif(e.get()=="hi"):
        txt.insert(END,"\n"+"Bot => Hello")
    elif(e.get()=="how are you"):
        txt.insert(END,"\n"+"Bot => Fine, and you?")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"Bot => Nice to hear!")
    elif(e.get()=="thank you"):
        txt.insert(END,"\n"+"Bot => No problem!")
    elif(e.get()=="what is your favourite book"):
        txt.insert(END,"\n"+"Bot => I can't read :(")
    elif(e.get()=="what is your favorite color"):
        txt.insert(END,"\n"+"Bot => Blue!")
    elif(e.get()=="who are you"):
        txt.insert(END,"\n"+"Bot => Who? Who is but a form following the function of what")
    elif(e.get()=="what are you then"):
        txt.insert(END,"\n"+"Bot => A man in a mask.")
    elif(e.get()=="what is your favorite movie"):
        txt.insert(END,"\n"+"Bot => Alice in Wonderland")
    elif(e.get()=="tell me about yourself"):
        txt.insert(END,"\n"+"Bot => What do you want to know?")
    elif(e.get()=="are you a robot"):
        txt.insert(END,"\n"+"Bot => Yes I am.")
    elif(e.get()=="how do you work"):
        txt.insert(END,"\n"+"Bot => It's complicated.")
    elif(e.get()=="are you a programmer"):
        txt.insert(END,"\n"+"Bot => Of course I am a programmer.")
    elif(e.get()=="what languages do you like to use"):
        txt.insert(END,"\n"+"Bot => I use Python, Java, and C++")
    elif(e.get()=="what annoys you"):
        txt.insert(END,"\n"+"Bot => A lot of things, like all the other digits other than 0 and 1.")
    else:
        txt.insert(END,"\n"+"Bot => Sorry I didn't get it.")
    e.delete(0,END)

def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        audio = r.listen(source)
        MyText = r.recognize_google(audio)
        send="You => " +MyText
    txt.insert(END,"\n"+send)
    if(MyText=="hello"):
        txt.insert(END,"\n"+"Bot => Hi")
    elif(MyText=="hi"):
        txt.insert(END,"\n"+"Bot => Hello")
    elif(MyText=="how are you"):
        txt.insert(END,"\n"+"Bot => Fine, and you?")
    elif(MyText=="fine"):
        txt.insert(END,"\n"+"Bot => Nice to hear!")
    elif(MyText=="thank you"):
        txt.insert(END,"\n"+"Bot => No problem!")
    elif(MyText=="what is your favourite book"):
        txt.insert(END,"\n"+"Bot => I can't read :(")
    elif(MyText=="what is your favourite colour"):
        txt.insert(END,"\n"+"Bot => Blue!")
    elif(MyText=="who are you"):
        txt.insert(END,"\n"+"Bot => Who? Who is but a form following the function of what")
    elif(MyText=="what are you then"):
        txt.insert(END,"\n"+"Bot => A man in a mask.")
    elif(MyText=="what is your favourite movie"):
        txt.insert(END,"\n"+"Bot => Alice in Wonderland")
    elif(MyText=="tell me about yourself"):
        txt.insert(END,"\n"+"Bot => What do you want to know?")
    elif(MyText=="are you a robot"):
        txt.insert(END,"\n"+"Bot => Yes I am.")
    elif(MyText=="how do you work"):
        txt.insert(END,"\n"+"Bot => It's complicated.")
    elif(MyText=="are you a programmer"):
        txt.insert(END,"\n"+"Bot => Of course I am a programmer.")
    elif(MyText=="what languages do you like to use"):
        txt.insert(END,"\n"+"Bot => I use Python, Java, and C++")
    elif(MyText=="what annoys you"):
        txt.insert(END,"\n"+"Bot => A lot of things, like all the other digits other than 0 and 1.")
    else:
        txt.insert(END,"\n"+"Bot => Sorry I didn't get it.")
    e.delete(0,END)   
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
txt.configure(bg = 'orange')
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
voice=Button(root,text="Voice",command=voice).place(x=604,y=363)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()
