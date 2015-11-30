import sys
import re
#[^b]*[b][^o]*[o][^a]*[a][^t]*[t](.?)

#([^char]*[char])*(.?) <- general regex

#structure of regex, each character is [^(char)]*[(char)]
#this captures everything that isn't the character until you hit the character then moves to the next state
#you can create a "string" of these in regex to see if you can find the given string within a larger document,
#perhaps hidden somewhere

#this will find the first such occurance.

#takes in a string as input

"""
If any group is captured (even an empty one) that means we got a hit!
It might been stretched across the entire document but YAY.
"""


def regexBuild(string):
    regex = ""
    for char in string:
        regex += "[^{0}]*[{0}]".format(char) 
    regex += "(.)"
    p = re.compile(regex)
    return p
def find(reg):
    try:
        filename = sys.argv[2]
    except:
        print('Need filename arg')
    try:
        f = open(filename,'r')
        words = f.read()
        m = reg.match(words)
        print(m)
        if m:
            print('Found Match')
        else:
            print('No Match')
    except:
        print("File not found")

reg = regexBuild(sys.argv[1])
find(reg)