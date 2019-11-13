host = 'http://hdyss.wasu.cn:8084/isearch_ol/search/personSearch?'
host2 = 'http://hdyss.wasu.cn:8084/isearch_ol/search/contentSearch?'
nodesc = '描述---暂无'
noprofess = '无专业'
noimg = '无头像'
noname = '无名字'
nopush = '无推荐'
header = {
    "User-Agent": "Mozilla/5.0",
    "usetype": "1",
    "sitecode": "iptvtest",
    "vsitecode": "hzvsite",
    "encodingprofile": "utf-8",
    "authflag": "1",
    "showtype": "36,37",
    "pageIndex": "1",
    "pageItems": "100"}
failall = []
nopushall = []
noDefindId = []
noImage = []
noDesc = []
noName = []
noProfess = []
passall = []


def gethost():
    return host


def gethost2():
    return host2


def getnodesc():
    return nodesc


def getnoprofess():
    return noprofess


def getnoimg():
    return noimg


def getnoname():
    return noname


def getnopush():
    return nopush


def getheader():
    return header


def getfail():
    return failall


def getpass():
    return passall
