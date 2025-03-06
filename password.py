import random
import string


pass_len=12
charValue = string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(pass_len):
    password = password + random.choice(charValue)

print("your random password is:",password)
