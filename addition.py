msg = ('simple calculator')
input(type('simple calculator'))
print(msg)
print(type(msg))

num1 = int(input("Enter the first number: "))
operator = input("Enter the operator(+, -, *, /): ")
num2 = int(input("Enter the second number: "))
result = 0  

if operator == '+':
   result= num1 + num2
elif operator == '-':
   result= num1 - num2
elif operator == '*':
   result= num1 * num2
elif operator == '/':
   result= num1 / num2 

print(f"{num1} {operator} {num2} = {result}")