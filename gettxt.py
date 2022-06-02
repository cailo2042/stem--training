from ssl import SSL_ERROR_WANT_X509_LOOKUP
from tkinter import*
root=Tk()
#create text field space
e1=Entry(root,width=50,bg='white',fg='black')
e1.pack()
e1.insert(0,"Enter first number,")

#second input
e2= Entry(root,width=50,bg='white',fg='black')
e2.pack()
e2.insert(0,"Enter second number.")

#create a task function
def myClick():
    f_no=float(e1.get())
    s_no=float(e2.get())
    sub=f_no-s_no
    add=f_no+s_no
    divis=f_no/s_no
    mult=f_no*s_no


    ANS="Add:"+ str(add)+ "\n sub:"+str(sub)+"\n divis:"+str(divis)+"\n mult:" +str(mult)
    My_Label =Label(root,text=ANS)
    My_Label.pack()
#Create a frame
my_Button = Button (root,text="answer",command =myClick,bg='white', fg='grey')
#show it on screen
my_Button.pack()
root.mainloop()
