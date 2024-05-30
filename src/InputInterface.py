from tkinter import *
import time
import requests

root=Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False,False)

heading=Label(root,text="Timer",font="arial 30 bold",bg="#000",fg="#ea3548")
heading.pack(pady=10)

#clock
Label(root,font=("arial",15,"bold"),text="Current Time:",bg='papaya whip').place(x=65,y=70)

def clock():
    clock_time=time.strftime("%H:%M:%S %p")
    current_time.config(text=clock_time)
    current_time.after(1000,clock)


current_time=Label(root,font=("arial",15,"bold"),text="",fg="#000",bg="#fff")
current_time.place(x=190,y=70)
clock()

#timer
##Hrs
hrs=StringVar()
Entry(root,textvariable=hrs,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=30,y=155)
hrs.set("00")

##Min
mins=StringVar()
Entry(root,textvariable=mins,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=150,y=155)
mins.set("00")

##Sec
sec=StringVar()
Entry(root,textvariable=sec,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=270,y=155)
sec.set("00")

Label(root,text="Hours",font="arial 12",bg="#000",fg="#fff").place(x=105,y=200)
Label(root,text="Mins",font="arial 12",bg="#000",fg="#fff").place(x=225,y=200)
Label(root,text="Secs",font="arial 12",bg="#000",fg="#fff").place(x=345,y=200)

def Timer():
    times=int(hrs.get())*3600+int(mins.get())*60+int(sec.get())
    while times> -1:
        minute ,second= (times//60,times%60)
        hour=0
        if minute>60:
            hour,minute=(minute//60,minute%60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if (times==0):
            print("Ready to play sound")
            print("Timer is 0. Fetch status again and then set the timer")
            sec.set("55")
            mins.set("00")
            hrs.set("00")
            Timer()
        
        times -= 1

def updateTrendStatus(userInput):
    if userInput=="1":
        r = requests.get("http://127.0.0.1:8000/apis/updateTrendStatus?updateTrendStatus=true&trendStatus=1")
        print(r.status_code)
        userInput="Up Trending"
    elif userInput=="2":
        r = requests.get("http://127.0.0.1:8000/apis/updateTrendStatus?updateTrendStatus=true&trendStatus=2")
        print(r.status_code)
        userInput="Down Trending"
    elif userInput=="3":
        r = requests.get("http://127.0.0.1:8000/apis/updateTrendStatus?updateTrendStatus=true&trendStatus=3")
        print(r.status_code)
        userInput="Ranging"
    elif userInput=="4":
        r = requests.get("http://127.0.0.1:8000/apis/updateTrendStatus?updateTrendStatus=true&trendStatus=4")
        print(r.status_code)
        userInput="Exiting the App"
        i=2
    elif userInput=="5":
        r = requests.get("http://127.0.0.1:8000/apis/fetchTrendStatus?fetchTrendStatus=true")
        print(r.status_code)
        print(r.headers)
        print(r.content)
        print(r.text)
        userInput="Ranging"
    else:
        userInput="Wrong Input"
    return userInput


def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")
    requestStatus=updateTrendStatus(userInput="1")
    print("The returned User Input is :",requestStatus)

def face():
    hrs.set("00")
    mins.set("15")
    sec.set("00")
    requestStatus=updateTrendStatus(userInput="2")
    print("The returned User Input is :",requestStatus)

def eggs():
    hrs.set("00")
    mins.set("10")
    sec.set("00")
    requestStatus=updateTrendStatus(userInput="3")
    print("The returned User Input is :",requestStatus)


def fetchTrendStatus():
    requestStatus=updateTrendStatus(userInput="5")
    print("The returned User Input is :",requestStatus)





#These 3 buttons can be created using photoshop. Size of the images is 127x127
Image1=PhotoImage(file="D:\scalpingInputInterface\ScalpingInputInterface\src\images\\upTrending.png")
button1=Button(root,image=Image1,bg="#000",bd=0,command=brush)
button1.place(x=7,y=300)

Image2=PhotoImage(file="D:\scalpingInputInterface\ScalpingInputInterface\src\images\\face.png")
button2=Button(root,image=Image2,bg="#000",bd=0,command=face)
button2.place(x=137,y=300)


Image3=PhotoImage(file="D:\scalpingInputInterface\ScalpingInputInterface\src\images\eggs.png")
button3=Button(root,image=Image3,bg="#000",bd=0,command=eggs)
button3.place(x=267,y=300)


button=Button(root,text="Fetch Trend Status",bg="#ea3548",bd=0,fg="#fff",width=15,height=2,font="arial 10 bold",command=fetchTrendStatus)
#button.pack(padx=55,pady=40,side=BOTTOM)
button.place(x=25,y=500)

buttonStartTimer=Button(root,text="Start",bg="#ea3548",bd=0,fg="#fff",width=15,height=2,font="arial 10 bold",command=Timer)
buttonStartTimer.place(x=175,y=500)


root.mainloop()