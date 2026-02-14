filenames = ["1.Print1.txt" , "2.Print2.txt" , "3.Print3.txt"]

for filename in filenames:
    filename = filename.replace('.','-',1)   # 1 here is the position of 1.print.txt
    print(filename)                                         #mutability means replace from one string to all of strings
