from tkinter import *
root=Tk()
import calendar

def shcal():
    window=Tk()
    window.title("whats happinning")
    window.geometry("550x600")
    year=int(e.get())
    content=calendar.calendar(year)
    text=Text(window,font="consolas 10",height=60,width=80)
    text.insert("1.0",content)
    text.pack()
    mainloop()



root.title("calendar")
l1=Label(root,text="Calendar",font=("times new roman",40,"normal"),bg="light blue")
l1.pack()

l2=Label(root,text="Enter here",font=("times new roman",20,"normal"))
l2.pack(pady=15)

e=Entry(root,width=20)
e.pack(pady=15)

c=Button(root,text="Submit",bg="red",command=shcal)
c.pack(pady=2)

exit=Button(root,text="Exit",bg="red")
exit.pack(pady=5)












mainloop()