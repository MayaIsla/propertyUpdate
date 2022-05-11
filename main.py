import difflib
#source = s.txt

#request = t.txt

source = 'port = 443'
request = 'port = 500'

varSource = source.partition('=')[0] #this is port
varRequest = request.partition('=')[0] #this is port

valSource = source.partition('=')[2] #this is 443
valRequest = request.partition('=')[2] #this is 500

#for line in difflib.unified_diff(
#    source, request, to = output, lineterm = ''):
#        print(line)


if (varRequest + ' = ' + valSource != varSource + ' = ' + valRequest):
   finalOutput = (varRequest + ' = ' + valRequest) #will be .replace since variables are the same.
   print(finalOutput)

if (varRequest  in source):
    print(finalOutput)

