from tkinter import*
root=Tk()
#create a task function
def myClick():

    My_Label =Label(root,text="Hey!, You clicked me!")
    My_Label.pack()
#Create a frame
my_Button = Button (root,text="click me",command =myClick ,bg='#800000',fg='#00FFFF')
#show it on screen
my_Button.pack()
root.mainloop()
