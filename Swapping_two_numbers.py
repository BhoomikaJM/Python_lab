
firstNum = int(input("Enter the score of plyer 1: "))
secondNum = int(input("Enter the score of player 2: "))
print(f"Before swapping.\n First number = '{firstNum}\n and player 1's score = '{secondNum}.")
temporary = firstNum
firstNum = secondNum
secondNum = temporary
print(f"After swapping.\n First number = '{firstNum}\n and player 2's score = '{secondNum}.")