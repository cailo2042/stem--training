# if statement.
x=0
if x>=1:
    print(" Hey I'm still here")
    x-=1
    print(x)
print("Done")
# else statement
x=10
if x==10:
   print(x)
else :
    print("Not 10") 

# elif to create grading system
grade = int(input("write student score"))
if grade >80 and grade <=100:
    print("student got an A") 
elif   grade >=70 and grade <80:
    print(" student got a B")   
elif   grade >=60 and grade <70:
    print("student got a C")  
elif   grade>=50 and grade <60:
    print("student got a D")
elif   grade>=40 and grade <50:   
    print("student got a E")          
else:
    print("invalid grade")

