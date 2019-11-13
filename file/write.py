from local import data
from local.data import nopushall, noImage, noProfess, noName, noDesc, noDefindId


def results():
    with open('../results/pass.txt', 'a+') as f:
        for i in data.getpass():
            f.writelines(i + '\n')
            data.getpass().remove(i)
    with open('../results/fail.txt', 'a+')as f:
        for i in data.getfail():
            f.writelines(i + '\n')
            data.getfail().remove(i)

    with open('../results/nopush.txt', 'a+')as f:
        for i in nopushall:
            f.writelines(i + '\n')
            nopushall.remove(i)

    with open('../results/noid.txt', 'a+')as f:
        for i in noDefindId:
            f.writelines(i + '\n')
            noDefindId.remove(i)

    with open('../results/noimage.txt', 'a+')as f:
        for i in noImage:
            f.writelines(i + '\n')
            noImage.remove(i)
    with open('../results/nodesc.txt', 'a+')as f:
        for i in noDesc:
            f.writelines(i + '\n')
            noDesc.remove(i)

    with open('../results/noname.txt', 'a+')as f:
        for i in noName:
            f.writelines(i + '\n')
            noName.remove(i)

    with open('../results/noprofess.txt', 'a+')as f:
        for i in noProfess:
            f.writelines(i + '\n')
            noProfess.remove(i)