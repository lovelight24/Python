from tkinter import *
win = Tk()
label1=Label(win,text="Label1",bg="Red")
label1.pack(fill=X)
label2=Label(win,text="Label2",bg="Green")
label2.pack()
label3=Label(win,text="Label3",bg="Yellow")
label3.pack(side=LEFT,fill=Y)
win.mainloop()