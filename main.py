import threading
from tkinter import *
import wikipedia as wiki
import pyttsx3

win = Tk()
win.geometry("1520x790+0+0")
win.title("Wiki Search App")
win.config(bg="#6dd0f7")

img = PhotoImage(file = "a.png")
back = Label(win,image=img,borderwidth=0)
back.pack()
back.place(x=0,y=0)

result = str()
loud = pyttsx3.init()

def speak__():
    global ent,loud
    loud.say(str(ent.get()))
    loud.runAndWait()

def speak_cont():
    global ent, loud, result
    result.split(".")
    loud.say(str(result))
    loud.runAndWait()
    
def clear():
    global text,ent
    text.delete(1.0,'end')
    ent.delete(0,'end')

def search(sear):
    global text,result
    text.delete(1.0,'end')
    if sear =="" or sear == " ":
        text.insert(INSERT, str("Please enter a valid keyword to search on wikipedia."))
    else:
        try:
            result = str(wiki.summary(sear, sentences = 10))
            text.insert(INSERT,str(result))
        except:
            text.insert(INSERT, str("Could not able to find ..."))

heading = Label(win, text="Wiki Search App",fg="#ffffff",bg="#6dd0f7", font=("bahnschrift semibold", 35), borderwidth=0)
heading.pack()
heading.place(x=100,y=30)

lab1 =Label(win,text="Topic: ",fg = "#ffffff",font=("bahnschrift semibold", 20), bg = "#6dd0f7")
lab1.pack()
lab1.place(x=100,y=120)

ent = Entry(win,font=("bahnschrift semibold", 20),bg = "lightcyan")
ent.pack()
ent.place(x=200,y=120)

img1 = PhotoImage(file = "d.png")
sear_but = Button(win, image=img1,bg="#6dd0f7", borderwidth=0,command=lambda:search(str(ent.get())))
sear_but.pack()
sear_but.place(x=600,y=120)

text = Text(win,font=("calibri", 17),bg = "white",width=110,height=18)
text.pack()
text.place(x=100,y=200)

img2=PhotoImage(file="c.png")
exit_but = Button(win, image=img2, borderwidth=0,bg="#6dd0f7", command=lambda:win.destroy())
exit_but.pack()
exit_but.place(x=100,y=720)

img3=PhotoImage(file="b.png")
clear_but = Button(win, image=img3, borderwidth=0,bg="#6dd0f7", command=clear)
clear_but.pack()
clear_but.place(x=700,y=120)

img4=PhotoImage(file="e.png")
spk_but = Button(win, image=img4, borderwidth=0,bg="#6dd0f7", command=speak__)
spk_but.pack()
spk_but.place(x=520,y=120)

spk_but1 = Button(win, image=img4, borderwidth=0,bg="#6dd0f7", command=lambda: threading.Thread(target=speak_cont).start())
spk_but1.pack()
spk_but1.place(x=40,y=200)

win.mainloop()
