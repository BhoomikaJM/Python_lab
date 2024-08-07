num = int(input("Enter a valid non-zero positive integer: "))
print(f"You have given an input of {num}")

if num <= 0:
    print("Please enter a valid non-zero positive integer.")
else:
    if num % 2 == 0:
        print(f"The given number {num} is Even.")
    else:
        print(f"The given number {num} is Odd.")