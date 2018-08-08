from tkinter import *

win = Tk()

label1 = Label(win,text="Name")
label2 = Label(win,text="Password")
entry1 = Entry(win)
entry2 = Entry(win,show="*")
label1.grid(row=0,sticky=E,ipadx=20,ipady=10)
label2.grid(row=1,sticky=E,ipadx=20,ipady=10)
entry1.grid(row=0,column=1,padx=10)
entry2.grid(row=1,column=1,padx=10)
c = Checkbutton(win,text="Keep me logged in!")
c.grid(columnspan=2)
win.mainloop()


