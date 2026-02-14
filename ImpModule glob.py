import glob

myfiles = glob.glob("*.txt")             #glob module has glob function used to locate all types of files in one go
                                         #and we can see on a particular file or all files whats inside
for filepath in myfiles:
    with open(filepath,'r') as file:
        print(file.read())              #we can print or capitalize or do anything from glob without opening all files one by one

