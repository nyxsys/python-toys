import json
import sys

def main():
    story = open(sys.argv[1],'r')
    
    doc = json.load(story)
    
    print(doc['result']['docs'][0]['source']['enriched']['url']['title'])
    print(doc['result']['docs'][0]['source']['enriched']['url']['url'])
    
main()