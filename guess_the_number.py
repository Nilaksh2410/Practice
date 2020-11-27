import random
num = random.randint(1,10)
guess = int(input("enter the number from 1 to 10 :"))
if num != guess:
    print("wrong guess!")
else:
    print("yuppie...!! its correct.")
