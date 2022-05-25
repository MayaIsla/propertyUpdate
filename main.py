import difflib
import re
from collections import Counter
import itertools

source = 'port = 443 \n corePoolSize = 500 \n theme = money'
request = 'port = 500 \n corePoolSize = 500 \n hello = world \n src = C:/Users/something.jar'

sourceFilePath = 'D:/Desktop/source.properties'
requestFilePath = "D:/Desktop/request.properties"

with open(sourceFilePath, 'r') as file1:  # compares source and request files.
    with open(requestFilePath) as file2:
        same = set(map(str.rstrip, file2)).difference(set(map(str.rstrip, file1)))

with open(sourceFilePath, 'a') as file_out, open(sourceFilePath, 'r') as file_in:
    for line in same:
        file_out.write("\n" + line)  # outputs and appends difference into source file.

lines = open(sourceFilePath, 'r').readlines()
lines_set = set(lines)
out = open(sourceFilePath, 'w')
for line in lines_set:
    out.write("\n" + line)  # string clean up in .properties file

file = open(sourceFilePath, 'rt+')
text = file.read()
file.close()


words = text.rstrip()


hello = [i.split('=', 1)[0] for i in words]

s = set(hello)
out = []
for i, z in enumerate(hello):
    if z in s:
        out.append(z)
        s.remove(z)
    else:
        break
    out += hello[i + 1:]

empty = []
for duplicate in hello:
    if duplicate not in empty:
        empty.append(duplicate)
    else:
        cleanDup = duplicate.replace(' ', '')

for l in words:
    if duplicate in words:
        words.remove(l)

# varSource = source.partition('=')[0] #this is port
# varRequest = request.partition('=')[0] #this is port

# valSource = source.partition('=')[2] #this is 443
# valRequest = request.partition('=')[2] #this is 500
# print(varRequest)

pair_list = source.split("\n")
list_pair = request.split("\n")

for pair in pair_list:
    valSource = pair.partition("=")[2]
    varSource = pair.partition("=")[0]
    sourceString = varSource + '=' + valSource
    for liste in list_pair:
        varRequest = liste.partition("=")[0]
        valRequest = liste.partition("=")[2]
        requestString = varRequest + ' = ' + valRequest
        sourceString = varSource + ' = ' + valSource
        # if (varRequest + ' = ' + valRequest  in varSource + ' = ' + valSource):
        # finalOutput = (varRequest + ' = ' + valRequest) #will be .replace since variables are the same.
        # print(finalOutput)
        # if (varRequest in source):
        # if (valRequest != valSource):
        # print(varRequest + '=' + valRequest) #replace

        # if varRequest not in source:  # do variables match up in source? if not in source file, append to bottom of source file.
        # print('"' + varRequest + '"' + ' Variable not in source file. (new variable)')

        # if varRequest in sourceString and valRequest not in sourceString:
        # finalOutput = (varRequest + ' = ' + valRequest) #will be .replace since variables are the same.
        # print(varRequest + '=' + valRequest)

# for liste in list_pair:
#    varRequest = liste.partition("=")[0]
#    valRequest = liste.partition("=")[2]

# requestString =  varRequest + '=' + valRequest
# print(requestString)
# sourceString = varSource + '=' + valSource
# print(sourceString)
