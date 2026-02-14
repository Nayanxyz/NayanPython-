import json

with open("question.json",'r') as file:
    content = file.read()

data = json.loads(content)           #loads if function to load


for question in data:                                       #bigger loop
    print(question["question_text"])
    for numb, alternative in enumerate(question["alternatives"]):
        print(numb +1,"-",alternative)

    user_choice = int(input("Enter your answer :"))
    question["user_choice"]= user_choice


score = 0                                                         #user has 0 value if value is correct it will add

for numb,question in enumerate(data):
    if question["user_choice"]== question["correct_answer"]:     #conditon if true
        score = score+1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = f"{numb+1} is {result} - Your answer: {question['user_choice']} correct Answer : {question['correct_answer']}"
    print(message)

print(f"{score} / {len(data)} SCORE")          #data has 2 dictionaries