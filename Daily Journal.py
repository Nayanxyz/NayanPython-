user = input("Enter today's date :")

mood = input("Rate your mood out of 10 :")


text = input("Let you thoughts flow :\n")

with open(f"Journal/{user}.txt",'w') as thought:
    thought.write(f"Your mood is {mood} today" + 2*"\n")
    thought.write(text)