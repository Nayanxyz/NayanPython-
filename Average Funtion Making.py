def get_average():
    with open('Data.txt','r') as file:
        temp = file.readlines()

    number = temp[1:]

    number = [float(i) for i in number]

    average_local = sum(number)/len(number)
    return average_local


average = get_average()
print(f"this is the average {average} degree Celcius")