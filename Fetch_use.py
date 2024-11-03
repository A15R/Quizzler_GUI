import json
import requests


class Question:
    def __init__(self):
        with open("questionn.json") as file:
            data = json.load(file)

        self.statement = data.pop()

        with open("questionn.json", "w") as file:
            json.dump(data, file)

        self.qstn = list(self.statement.keys())
        self.answer = list(self.statement.values())



class Sample:

    def __init__(self):
        self.sample = []
        self.url = "https://opentdb.com/api.php?amount=50&difficulty=medium&type=boolean"

    def get_questions(self):
        d = requests.get(self.url)
        data = d.json()["results"]
        for item in data:
            self.sample.append({item["question"]: item["correct_answer"]})
        with open("questionn.json", "w") as file:
            json.dump(self.sample, file)

x = Sample()
x.get_questions()