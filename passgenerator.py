import random

length = int(input("How long should the password be ? : "))

small = "abcdefghijklmnopqrstuvwxyz"
big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
symbols = "!@#$%^&*()-_=+[]{};:/?.<>"

all_chars = small + big + nums + symbols

password = ""
for i in range(length):
    password += random.choice(all_chars)

print("\nHere is your generated password:")
print(password)