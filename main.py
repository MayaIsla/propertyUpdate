import difflib
#source = s.txt

#request = t.txt

source = 'port = 443 \n corePoolSize = 500 \n theme = money'
request = 'port = 500 \n corePoolSize = 500 \n hello = world \n src = C:/Users/something.jar'

#varSource = source.partition('=')[0] #this is port
#varRequest = request.partition('=')[0] #this is port

#valSource = source.partition('=')[2] #this is 443
#valRequest = request.partition('=')[2] #this is 500
duplicateVariable = {}

#print(varRequest)

pair_list = source.split("\n")
list_pair = request.split("\n")

for pair in pair_list:
    valSource = pair.partition("=")[2]
    varSource = pair.partition("=")[0]
    sourceString = varSource + '=' + valSource
    for liste in list_pair:
        varRequest = liste.partition("=")[0]
        valRequest = liste.partition("=")[2]
        requestString =  varRequest + ' = ' + valRequest
        sourceString = varSource + ' = ' + valSource
       # if (varRequest + ' = ' + valRequest  in varSource + ' = ' + valSource):
            #finalOutput = (varRequest + ' = ' + valRequest) #will be .replace since variables are the same.
            #print(finalOutput)
       # if (varRequest in source):
            #if (valRequest != valSource):
                #print(varRequest + '=' + valRequest) #replace 
                
        if (varRequest not in source): #do variables match up in source? if not in source file, append to bottom of source file.
            print('"'+varRequest+'"' + ' Variable not in source file. (new variable)')
            
        if (varRequest in sourceString and valRequest not in sourceString):
            #finalOutput = (varRequest + ' = ' + valRequest) #will be .replace since variables are the same.
            print(varRequest + '=' + valRequest)
            
        
#for liste in list_pair:
#    varRequest = liste.partition("=")[0]
#    valRequest = liste.partition("=")[2]
   
#requestString =  varRequest + '=' + valRequest
#print(requestString)
#sourceString = varSource + '=' + valSource
#print(sourceString)

    



