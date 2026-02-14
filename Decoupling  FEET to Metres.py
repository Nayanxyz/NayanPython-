feet_inches = input("enter feet :")      #""" Doc strings are usefulll (ctrl +alt +B)"""

def feets(feet__inches):                                            #def convert(feet__inches):
    parts = feet__inches.split(" ")                                     #parts = feet__inches.split(" ")
    feet = float(parts[0])                                              #feet = float(parts[0])
    inches = float(parts[1])                                            #inches = float(parts[1])
    return feet , inches
                                                                        # meters = feet * 0.3048 + inches * 0.0254
                                                                        # return meters
def convert(feet,inches):
    meters = feet * 0.3048 + inches * 0.0254                            # result  = convert(feet_inches) ....same if else
    return meters
                                                                   #above code was heavy , thats why we use decoupling(splits)
                                                                   #to understand code easily


converting = feets(feet_inches)                          #calling feets def and input variable inside first
                                                         # then calling convert def inside converting[0] for feet argument..
result  = convert(converting[0], converting[1])          #..[1] for inches argument..

if result < 1:                                           #we can also do//   f , i = feets(feet_inches)
    print("Kid is too small.")                           #             //    result = convert(f,i)

else:
    print("Kid can go to slide.")                        #it means handling two variables at once possible

