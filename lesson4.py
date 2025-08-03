from tkinter import *
root=Tk()
root.geometry("250x250")
header=Label(root,text="ice cream",font=("times new roman",25,"normal"),bg="light blue")
header.pack()
#frames
f1=Frame(root,bg="pink",height="125")
f1.pack(fill=X,pady=20)
f2=Frame(root,bg="yellow",height="125")
f2.pack(fill=X,pady=50)


#button
b1=Button(f1,text="choclate",bg="Brown")
b1.grid(row=0,column=0,padx=10)
b2=Button(f1,text="strawberry",bg="pink")
b2.grid(row=0,column=1,padx=10)
b3=Button(f1,text="Vanilla",bg="yellow")
b3.grid(row=0,column=2,padx=10)

b4=Button(f2,text="mint",bg="green")
b4.grid(row=1,column=0,padx=10)
b5=Button(f2,text="bubblegum",bg="blue")
b5.grid(row=1,column=1,padx=10)
b6=Button(f2,text="mango",bg="orange")
b6.grid(row=1,column=2,padx=10)










mainloop()