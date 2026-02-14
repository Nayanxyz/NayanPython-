import csv            #csv is a text file with .csv extension this is usually split in columns

with open("Columns.csv", "r") as file:
    data = list(csv.reader(file))             #reader is function of csv module and then we iterate it with list[]

city = input("enter a city : ")

for row in data[1:]:                     #csv has first row that is row[0] city and row[1] is temperature
    if row[0] == city:                  #everytime i put a name of a city it gives me its value
       print(row[1])                 #also i see row[0] is names of headings .. so i give them value of a city name to row [0]