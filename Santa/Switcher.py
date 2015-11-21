__author__ = 'Mark'
import csv
import random
import os


def main():
    try:
        reader = csv.DictReader(open("naughty_list.csv", "r"))
    except:
        f = open("Failure.txt", 'w')
        f.write("Please create a naughty_list.csv before use.")
        exit(1)
    nList = [row for row in reader]
    random.shuffle(nList)



    match = []
    for name in nList:
        match.append([name["Name"]])


    bufferNList = nList+nList
    for i in range(len(match)):
        addNext(i, match, bufferNList, 2)
        addNext(i, match, bufferNList, 4)

    write(match)

def addNext(santa,match, nList, shift):
    match[santa].append(nList[santa+shift])


def write(santaList):
    directory = "./assignment/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for santa in santaList:
        f = open(directory + santa[0]+"_Assignment.txt", 'w')
        f.write("Hello and Welcome to Dickory Dock 2015!\n\n")
        f.write("{0}, your assignments are as follows:\n".format(santa[0]))
        f.write("\t {0}, who would like {1}\n".format(santa[1]["Name"], santa[1]["Wishlist"]))
        f.write("\t {0}, who would like {1}\n\n".format(santa[2]["Name"], santa[2]["Wishlist"]))
        f.write("MERRY CHRISTMAS")


main()