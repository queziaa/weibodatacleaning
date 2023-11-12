# encoding=utf-8
import json

tSet = {}
outset = {}
s = 0
t = 0
with open('爬取用户信息合并.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        s = s + 1
        obj = json.loads(line)
        if obj['_id'] in tSet:
            t = t + 1
        else:
            tSet[obj['_id']] = 1
print("已经爬取用户信息：" + str(s))
print("去重后：" + str(t))
print(str(t / s * 100) + '%')

s = 0
t = 0
b = 0
with open('../1爬取关键词微博/爬取关键词微博.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        s = s + 1
        obj = json.loads(line)
        Tid = obj['user']['_id']
        if Tid in tSet:
            t = t + 1
        else:
            outset[Tid] = 1
            b = b + 1

with open('待爬取用户信息ID表.txt', 'w', encoding='UTF-8') as out:
    for key in outset:
        out.write(key + '\n')

print("关键词博文数量" + str(s))
print("用户信息已爬取" + str(t))
print("待带爬取数量" + str(b))
print(len(outset))
print(str(t / s * 100) + '%')