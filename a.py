import random

target=random.randint(1,100)

while True:
    userNumber = int(input("guess the target :"))
    if(userNumber == target):
        print("success : correct guess!!")
        break
    elif(userNumber < target):
        print("number was too samm .take a bigger guess..!!")
    else:
        print("your number is too big.take a smaller guess..!!")
    

print("---Game over---")

