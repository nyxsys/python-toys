from lxml import html
import requests
import random
import datetime

try:
    page = requests.get('http://www.nationalpastime.com')
except :
    print("Bad Connection")
    quit()

tree = html.fromstring(page.text)
dates = tree.xpath('//strong/text()')
facts = tree.xpath('//td/text()')

dates.pop(0)

i=0
curlen= len(facts)
while(i<curlen):
    if(facts[i].isspace()):
        facts.pop(i)
        curlen=len(facts)
    else:
        i+=1


today = datetime.date.today()

i = random.randint(0,len(facts))


print
print("In the year", (dates[i].strip()),"on", today.strftime("%b %d"))
print(facts[i].strip())
print




