
import requests


try:
    page = requests.get('https://piratrad.io/random')
except :
    print("Bad Connection")
    quit()

print(page.url)