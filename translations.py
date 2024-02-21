import json
from os import system


def LoadFile(fileName):
    with open(fileName,'r') as file:
        temp=json.load(file)
    return temp


def SaveFile(fileName,jsonDict):
    with open(fileName, "w") as file: 
        json.dump(jsonDict, file, indent=4)


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
                elif isinstance(dic1[x],dict) and isinstance(dic2[x],str):
                    dic1[x]=dic2[x]
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


def Menu():
    system('clear')
    print('1.Check file')
    print('2.New file')
    inp=input()
    match(inp):
        case '1':
            CheckFile()
        case '2':
            NewFile()


def CheckFile():
    system('clear')
    dictPL=LoadFile(input('"Pattern" file name (PL): '))
    system('clear')
    dictTr=LoadFile(input('Translations file name: '))  

    dictTr=FindMissing(dictTr,dictPL)
    dictTr=TagIncorrect(dictTr,dictPL)

    dictTr=Sort(dictTr,dictPL)

    system('clear')
    SaveFile(input('Name of saved file: '),dictTr)


def NewFile():
    system('clear')
    dictPL=LoadFile(input('"Pattern" file name (PL): '))
    dictPL=ReplaceValue(dictPL)
    
    system('clear')
    SaveFile(input('Name of saved file: '),dictPL)
    system('clear')


Menu()