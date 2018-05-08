import os
import os.path

l = []


def get_py(path, l):
    fileList = os.listdir(path)  # 获取path目录下所有的文件
    for filename in fileList:
        pathTmp = os.path.join(path, filename)  # 获取path和filename组合后的路径
        if os.path.isdir(pathTmp):  # 如果是目录
            get_py(pathTmp, l)  # 则递归查找
        elif filename[-3:].upper() == ".PY":  # 不是目录，则比较后缀名
            l.append(pathTmp)


path = input("请输入路径：").strip()
get_py(path, l)
print("在%s目录及其子目录下找到%d个py文件\n分别为：\n" % (path, len(l)))
for filepath in l:
    print(filepath)
