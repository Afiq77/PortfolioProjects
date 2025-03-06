import random

target=random.randint(1,100)

print(target)

while True:
    userNumber = input("guess the target or Quit :")
    if (userNumber == "Quit"):
        break
    userNumber = int(userNumber)
    if(userNumber == target):
        print("success : correct guess!!")
        break

    elif(userNumber < target):
        print("number was too small .take a bigger guess..!!")
        
    else:
        print("your number is too big.take a smaller guess..!!")
    

print("---Game over---")