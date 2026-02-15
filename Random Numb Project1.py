import random

print("Enter Random Number!!")
try:
    user_min = int(input("Enter smaller digit : "))
    user_max = int(input("Enter large digit : "))

    number = random.randint(user_min,user_max)
    print(f"random number : {number}")

except ValueError:
    print("type min value first and Rerun !")
