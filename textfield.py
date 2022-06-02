from tkinter import*

root=Tk()
e=Entry(root,width=50,bg="black",fg="green")
e.pack()
#create a task function
def myClick():
    Hello="Hello"+ e.get()
    My_Label =Label(root,text=Hello)
    My_Label.pack()

#Create a frame
my_Button = Button (root,text="click me",command =myClick ,bg='#800000',fg='#00FFFF')
#show it on screen
my_Button.pack()
root.mainloop()
