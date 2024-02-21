import json
filePL = open('pl-PL.json','r')
dictPL = json.load(filePL)
filePL.close()

fileEN = open('en-EN.json','r')
dictEN = json.load(fileEN)
fileEN.close()


def TagIncorrect(dic1,dic2):
    for x in dic1.keys():
        if x not in dic2.keys() or type(dic1[x]) is not type(dic2[x]):
            dic1[x]='REMOVETHIS'
        else:
            if isinstance(dic1[x],dict):
                dic1[x]=TagIncorrect(dic1[x],dic2[x])
    return dic1


def FindMissing(dic1,dic2):
    dic2=ReplaceValue(dic2)
    for x in dic2.keys():
        if isinstance(dic1,dict):
            if x in dic1.keys():
                if isinstance(dic2[x],dict):
                    dic1[x]=FindMissing(dic1[x],dic2[x])
            else:
                dic1[x]=dic2[x]
        else:
            dic1=dic2
    return dic1


def ReplaceValue(dic):
    for x in dic:
        if not isinstance(dic,str):
            if not isinstance(dic[x],dict):
                dic[x]="TODO"
            else:
                dic[x]=ReplaceValue(dic[x])
    return dic
        

def Sort(dic1,dic2):
    temp={}
    for x in dic2.keys():
        temp[x]=dic1[x]
    return temp

    

dictEN=TagIncorrect(dictEN,dictPL)
dictEN=FindMissing(dictEN,dictPL)

res=Sort(dictEN,dictPL)


with open("test.json", "w") as outfile: 
    json.dump(res, outfile, indent=4)