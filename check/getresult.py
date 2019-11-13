import json

import requests
from retry import retry
from local import data as localdata

from local.data import host2, nopush, host, header, nodesc, failall, noname, noprofess, passall, noDesc, noImage, \
    noName, noProfess, noDefindId, nopushall


# 获取返回数据中的name字段


def getname(result):
    name = result[0]['name']
    return name


# 获取返回数据中的professional字段
def getprofess(result):
    profess = result[0]['professional']
    return profess


# 获取返回数据中的desc字段
def getdesc(result):
    desc = result[0]['description']
    return desc


# 获取返回数据中的smallimage字段
def getimg(result):
    img = result[0]['smallimage']
    return img


# 循环ID获取返回数据
@retry((TimeoutError, ConnectionRefusedError), tries=10, delay=10)
def getres(personid, aod, flag, location):
    for person, name in zip(personid, aod):
        location2 = location + 1
        header.update({'aod': name})
        print(name)
        push(header, person, name)
        url = geturl(person)
        result = getresults(url)
        if len(result) != 0:
            desc = getdesc(result)
            imgurl = getimg(result)
            name = getname(result)
            profess = getprofess(result)
            if desc == '暂无':
                failmsg = person + name + nodesc
                noDesc.append(failmsg)
                failall.append(failmsg)
                flag += 1
            # if desc == '':
            #     failmsg = person + name + nodesc
            #     noDesc.append(failmsg)
            #     failall.append(failmsg)
            #     flag += 1
            if imgurl == '':
                imgfail = person + name + '无图'
                noImage.append(imgfail)
                failall.append(imgfail)
                flag += 1
            if imgurl != '':
                flag += imgtest(imgurl, person, name)
            if name == '':
                failmsg = person + name + noname
                noName.append(failmsg)
                failall.append(failmsg)
                flag += 1
            if profess == '':
                failmsg = person + name + noprofess
                noProfess.append(failmsg)
                failall.append(failmsg)
                flag += 1
            if flag == 0:
                passmsg = person + ' ' + name + 'pass啦!'
                passall.append(passmsg)
        else:
            nullmsg = person + name + '当前personid未定义'
            failall.append(nullmsg)
            noDefindId.append(nullmsg)



# 发送请求，获取返回数据
@retry((TimeoutError, ConnectionRefusedError), tries=10, delay=10)
def getresults(url):
    s = requests.session()
    # s.proxies = {'http': '120.92.178.3:8111', 'https': '114.141.155.27:8111'}
    s.keep_alive = False
    reqresult = s.get(url)
    if reqresult.status_code != 200:
        raise requests.RequestException('error')
    result = reqresult.json()['results']
    return result


# 通过ID组合请求URL
def geturl(person):
    url = host + 'personid=' + str(person)
    return url


# samllimage 检验
def imgtest(imgurl, person, name):
    imgreq = requests.get(imgurl)
    text = imgreq.headers
    texts = text['Content-Type']
    if texts == 'text/html':
        imgfail = person + name + '无图'
        failall.append(imgfail)
        return 1
    else:
        return 0


# @retry((TimeoutError, ConnectionRefusedError), tries=10, delay=10)
def push(head, personid, name):
    data = json.dumps(head)
    s = requests.session()
    # s.proxies = {'http': '120.92.178.3:8111', 'https': '114.141.155.27:8111'}
    s.keep_alive = False
    r = s.post(host2, data=data)
    if r.status_code != 200:
        raise requests.RequestException('error')
    result = json.loads((r.text))
    num = len(result['results'])
    if num != 0:
        # print(personid + name
        pass
    else:
        fail = failall
        failmsg = personid + name + nopush
        fail.append(failmsg)
        nopushall.append(failmsg)
