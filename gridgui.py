#GUI with python
from tkinter import*
root=Tk()
#show it on screen
my_label1= Label (root,text="Hello World!")
my_label2= Label (root,text="Hello World!")
#show it on screen
my_label1.grid (row=0,column=0)
my_label2.grid (row=0,column=0)
root.mainloop()