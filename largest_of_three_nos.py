firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))
thirdNum = int(input("Enter third number: "))

if firstNum > secondNum and firstNum > thirdNum:
    print("The first number is greatest.")
elif secondNum > firstNum and secondNum > thirdNum:
    print("The second number is greatest.")
else:
    print("The third number is greatest.")