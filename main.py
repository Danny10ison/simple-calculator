"""A simple calculator

More explanation
"""

# Give a welcome prompt
# Take user input
# perform operations
# display result to user

# variable to hold welcom prompt
msg = "Simple calculator"

# check the type of the variable
# print(type(msg))
print(msg)

num1 = int(input("Enter the first number: "))
operator = input("Enter the operator(+, -, *, /): ")
num2 = int(input("Enter the second number: "))
result = 0


# compare the operator here
if operator == '+':
    # do addition here
elif operator == '-':
    result= num1 - num2
elif operator == '*':
    # do multiplication here
    result = num1 * num2
elif operator == '/':
    # do division
    result = num1 / num2
    
else:
    print("Wrong operator")


# print("num1")
print(f"{num1} {operator} {num2} = {result}")
