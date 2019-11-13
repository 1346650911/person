import json
from local import data


def getperson(flag):
    slist = []
    f = open("../local/test.json", encoding='utf-8')
    person = json.load(f)
    # print(len(person))
    # print(person[0])
    for i in person[flag:flag + 30]:
        # print(i)
        if 'id' in i:
            personid = i['id']
            slist.append(str(personid))
        else:
            test = data.getfail()
            test.append(i['name'] + '   没有提供ID')
    return slist


def getaod(fl):
    slist = []
    f = open("../local/test.json", encoding='utf-8')
    person = json.load(f)

    for i in person[fl:fl + 30]:
        if 'name' in i:
            aod = i['name']
            slist.append(str(aod))
        else:
            test = data.getfail()
            test.append(i['name'] + '   没有提供ID')
    return slist

# class read():
#     pass
