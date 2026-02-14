mylist = ['zzz', 'aaa' ,'rrr']
mylist.sort()              #ascending order alphabetically

#mylist.sort(reverse=True)  for descending order

for i , words in enumerate(mylist):
    symb = f"{i +1} -{words}"
    print(symb)