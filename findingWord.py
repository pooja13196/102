import os
import shutil

file_name = input('Enter you file name: ')
f = open(file_name)
file_lines = f.readlines()

found = False

search_string = input('Enter the word you want to search: ')
for lines in file_lines:
    print(lines)
    words = lines.split()
    for word in words:
        if(word == search_string):
            found = True

if(found == True):
    print('Word is present')

else:
    print('Word is not present')