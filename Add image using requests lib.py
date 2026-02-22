import requests

url = ("https://images.pexels.com/photos/36717/"
       "amazing-animal-beautiful-beautifull.jpg?cs=srgb&dl=pexels-pixabay-36717.jpg&fm=jpg")
response = requests.get(url)

#response.text used for web pages that are texts



with open("image.jpg", "wb") as file:
    file.write(response.content)

    #we can download an image using url