first_no = input("Enter the first number : ")
operator = input("Enter the operator(+,-,*,/,%) : ")
second_no = input("Enter the second number : ")

if operator == '+':
    print("Sum = "+str(int(first_no) + int(second_no)))

elif operator == '-':
    print("Diff = "+str(int(first_no) - int(second_no)))

elif operator == '*':
    print("Product = "+str(int(first_no) * int(second_no)))

elif operator == '/':
    print("Div = "+str(int(first_no) / int(second_no)))

elif operator == '%':
    print("Modulous = "+str(int(first_no) % int(second_no)))
else:
    print("Enter an valid operator...!")

    #Output:

#Enter the first number : 5
#Enter the operator(+,-,*,/,%) : %
#Enter the second number : 5
#Modulous = 0

#Enter the first number : 5
#Enter the operator(+,-,*,/,%) : >
#Enter the second number : 6
#Enter an valid operator...!