password = input("Enter Password : ")

result = []
if len(password) >=8:
    result.append(True)
else:
    result.append(False)

number = False
for i in password:
    if i.isdigit():               #strng method for checking ints
        number = True

result.append(number)

uppercase = False

for i in password:
    if i.isupper():              #str method for checking uppercase chars   .upper returns capital version of str
        uppercase = True                                                   # but .isupper return boolean version(T/F)

result.append(uppercase)


if all(result):                   #==True default        all = Return True if bool(x) is True for all values x in the iterable.
    print("Strong Password")
else :
    print("Weak Password")