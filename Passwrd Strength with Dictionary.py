password = input("Enter Password : ")

result = {}                          #{} dictionary symbol ...dictionaries are list of different elements like str,int,etc
if len(password) >=8:
    result["length"]= True
else:
    result["length"]= False

number = False
for i in password:
    if i.isdigit():               #strng method for checking ints
        number = True

result["number"]= number

uppercase = False

for i in password:
    if i.isupper():              #str method for checking uppercase chars   .upper returns capital version of str
        uppercase = True                                                   # but .isupper return boolean version(T/F)

result["uppercase"]= uppercase


if all(result.values()):         #.values shows dict. value   all = Return True if bool(x) is True for all values x in the iterable.
    print("Strong Password")     #if want to see print(result) and print(result.values())
else :
    print("Weak Password")