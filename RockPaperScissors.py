import random


print("Starting Game",end='')

print("Welcome To Rock Paper Seissor Game")
print("1. Rock")
print("2. Paper")
print("3. Scissors")


x =random.randint(1,3)


y = int(input("Enter a number from given index: "))
if y>3:
    print("Number is not present")
    print("Exitting!")
    exit()
elif x == y:
    print("Draw")
    print(f"Computer choosed {x}")
elif x == 1 and y == 3:
    print("Sorry! You Lost") 
    print("Computer Choosed Rock")  
elif x == 2 and y == 1:
    print("Sorry! You Lost")
    print("Computer Choosed Paper")
elif x == 3 and y == 2:
    print("Sorry! You Lost")
    print("Computer Choosed Scissors")

else:
    print("Congratulations! You Win")

