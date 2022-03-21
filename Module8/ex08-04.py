import os
words = []
fileName = input('Please enter a file name to have the words counted: ')
try:
    print(fileName)
    fhand = open(fileName , 'r')
except:
    print("\n\nThere was a problem opening the file. Is {} in the current directory?\n'{}'".format(fileName, os.getcwd()))
    quit()
for line in fhand:
    for word in line.split(' '):
        if word not in words:
            word=word.strip()
            #This is how I would prefer to solve it(case insenstive)        words.append(word.lower())
            words.append()

print(sorted(words))
