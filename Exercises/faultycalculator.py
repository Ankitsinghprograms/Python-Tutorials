print("Simple Calculator\n")
print("Which Operator\n")
print("Addition,Substraction,Multiplication or Division\n")
print("Write the Operator name\n")
o=input()
operator=o.lower()
print("\n")
print("First Number\n")
a=int(input())
print("\n")
print("Second Number\n")
b=int(input())
print("\n")


#faulty calculator
if operator=="multiplication" and a==45 and b==3 or operator=="multiply" and a==45 and b==3 or operator=="×" and a==45 and b==4 or operator=="x" and a==45 and b==3 or operator=="multiplication" and a==3 and b==45 or operator=="multiply" and a==3 and b==45 or operator=="×" and a==3 and b==45 or operator=="x" and a==3 and b==45:
	print(555)

elif operator=="addition" and a==56 and b==9 or operator=="add" and a==56 and b==9 or operator=="+" and a==56 and b==9 or operator=="addition" and a==9 and b==56 or operator=="add" and a==9 and b==56 or operator=="+" and a==9 and b==56:
	print(77)

elif operator=="division" and a==56 and b==6 or operator=="divide" and a==56 and b==6 or operator=="÷" and a==56 and b==6 or operator=="/" and a==56 and b==6 or operator=="division" and a==6 and b==56 or operator=="divide" and a==6 and b==56 or operator=="÷" and a==6 and b==56 or operator=="/" and a==6 and b==56:
	print(4)
	
#real calculator starts
elif operator=="addition" or "add" or "+":
	print(a+b)
elif operator=="substraction" or "subtract" or "-":
	print(a-b)
elif operator=="muliplication" or "multiply" or "×" or "x":
	print(a*b)
elif operator=="division" or "divide" or "÷" "/":
	print(a/b)
else:
	print("Wrong operator\n")