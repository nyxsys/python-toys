import requests
import json



def main():
    doc = requests.get("http://jservice.io/api/clues?value=100")
    questions = json.loads(doc.text)
    for question in questions:
        print(question)
main()
