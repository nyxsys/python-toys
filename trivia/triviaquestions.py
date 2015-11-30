import requests
import json
import sys

        
def remain(i,limit):
    remaining = limit - i
    if remaining>0:
        return "{0} questions remain>".format(remaining)
    else:
        return "No questions left"

def main():
    try:
        doc = requests.get("http://jservice.io/api/random")

        category_id = json.loads(doc.text)[0]["category"]["id"]

        doc = requests.get("http://jservice.io/api/category?id="+str(category_id))
        questions = json.loads(doc.text)
        if(len(sys.argv) == 1):
            limit = 5
        elif(sys.argv[1].isdigit()):
            amount = int(sys.argv[1])
            if(amount >= len(questions["clues"])):
                limit = len(questions["clues"])
            else:
                limit = amount
        elif(sys.argv[1] == "-a"):
            limit = len(questions["clues"])
        else:
            limit = 5
    except Exception as e:
        print("\n {0} \n".format(e))
        exit()
    print("\n"+ questions["title"].upper() + "\n")

    i = 1
    for question in questions["clues"] :
        print("\nQuestion " + str(i) + "\n")
        print(question["question"] + "\n")
        input("Press enter for answer.")
        answer = question["answer"]
        answer = answer.replace("<\i>","")
        answer = answer.replace("<i>","")
        print("\n" + answer + "\n")
        a = input(remain(i,limit))
        i += 1
        if(a == "q" or i>limit):
            print("That's all folks!")
            exit()
main()