import json
def encapsule(path):
    temp=len(path.split('.'))
    path=path.replace('.','\':{\'')
    path=path.replace(': ','\':\'')
    path='{\''+path+'\''
    for x in range(temp):
        path=path+'}'
    return path

# def tets(path):
#     temp=path.split('.')
#     test[temp[0]]=tet(path.split('.')[1:])

# def tet(path):
#     if len(path)>1:
#         temp={}
#         temp[path[0]]=tet(path[1:])
#         return temp
#     else:
#         test={}
#         test[''.join(path)]='TODO'
#         return test





# def tets(dic,path):
#     path=path.split('.')
#     if len(path)>1:
#         if path[0] not in dic.keys():
#             dic[path[0]]=tet(path[1:])
#         else:
#             temp=dic[path[0]]
#             dic[path[0]][path[1]]=tet(path[2:])
#     else:
#         dic[path[0]]='TODO'

# def tet(path):
#     temp={}
#     if len(path)>1:
#         temp[path[0]]=tet(path[1:])
#         return temp
#     else:
#         temp[path[0]]='TODO'
#         return temp








test={'user':{'test':'tet'}}
tets(test,'user.edit.title')
tets(test,'user.edit.titl')
tets(test,'tet.test')
# test['user']={}
# tets('user.test')


with open("test.json", "w") as outfile: 
    json.dump(test, outfile, indent=4)