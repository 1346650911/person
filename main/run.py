import json
import time

import requests
from pyecharts.charts import Bar
from retry import retry
from pyecharts import options as opts
from check import getresult
from file import read
from file.write import results
from local.data import passall, failall, nopushall, noDefindId, noImage, noDesc, noName, noProfess


def run(test):
    for i in range(6990, 7200, 30):
        print('开始了--------------当前进度:' + str(i))
        person = read.getperson(i)
        aod = read.getaod(i)
        result = getresult.getres(person, aod, 0, test)
        results()
        time.sleep(1)


def readfile(filename):
    file = filename
    myfile = open(file)
    lines = len(myfile.readlines())
    return lines


# host2 = 'http://hdyss.wasu.cn:8084/isearch_ol/search/contentSearch?'
# header = {"usetype": "1",
#           "sitecode": "iptvtest",
#           "vsitecode": "hzvsite",
#           "encodingprofile": "utf-8",
#           "authflag": "1",
#           "showtype": "36,37",
#           "pageIndex": "1",
#           "pageItems": "100",
#           "aod": "古天乐"}


# def tese():
#     data = json.dumps(header)
#     r = requests.post(host2, data=data)
#     print(r.content)

#
# tese()
i = 0
run(i)
timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
bar = Bar()
bar.add_xaxis(['通过', '失败', '无推荐', 'ID未定义', '无图', '无描述', '无名字', '无职业'])
passnum = readfile('../results/pass.txt')
failnum = readfile('../results/fail.txt')
nopushnum = readfile('../results/nopush.txt')
noDefindnum = readfile('../results/noid.txt')
noImagenum = readfile('../results/noimage.txt')
noDescnum = readfile('../results/nodesc.txt')
noNamenum = readfile('../results/noname.txt')
noProfessnum = readfile('../results/noprofess.txt')
bar.add_yaxis('数量', [passnum, failnum, nopushnum, noDefindnum, noImagenum, noDescnum, noNamenum, noProfessnum])
bar.set_global_opts(title_opts=opts.TitleOpts(title='人物测试',subtitle=timenow))
bar.render()
