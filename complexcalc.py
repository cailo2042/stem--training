# Code
print("Welcome :Complex calculator")
first_number =input("Enter first number")
second_number =input("Enter second number")
# Re-declare and convert to integer
first_number =int(first_number)
second_number =int(second_number)
print("select an operator,options:[+,*,/,%,-]")
operator =input("Enter operator")
ans ="answer"
if '*'== operator:
    print(ans,first_number*second_number)
elif '+'== operator:
    print(ans,first_number+second_number)
elif '-'== operator:
    print(ans,first_number-second_number)
elif '/'== operator:
    print(ans,first_number/second_number)
elif '%'== operator:    
    print(ans,first_number%second_number)
else:
    print("Operator does not exist")
