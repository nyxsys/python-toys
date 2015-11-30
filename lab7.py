import itertools
import sys

try:
    subsets = []
    items = sys.argv[1]
    final = len(items)
    i = 0
    while(i<=final):
        temp = itertools.combinations(items,i)
        for item in temp:
            subsets += [list(item)]    
        i+=1
    print(subsets)

except:
    print("Bad Input")
    exit()