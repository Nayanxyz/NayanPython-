import webbrowser                                     #module is used for websearch

user = input("enter search :")                        #to replace spaces ().replace(" ","+") and have multiple words no issues

webbrowser.open("https://www.google.com/search?q=" + user)                #open is webbrowser function