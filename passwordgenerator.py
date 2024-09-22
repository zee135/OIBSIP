import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

string = lower+upper+numbers+symbols
length = int(input("enter a length"))
password = "".join(random.sample(string,length))

print("your password is :" + password)