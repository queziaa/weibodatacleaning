# encoding=utf-8
import json

tSet = {}
outset = {}
s = 0
t = 0
with open('../2爬取用户信息/由用户信息得到h黑名单.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        s = s + 1
        obj = int(line)
        if obj in tSet:
            t = t + 1
        else:
            tSet[obj] = 1
print("黑名单：" + str(s))
print("去重了：" + str(t))
print(str(t / s * 100) + '%')

s = 0
t = 0
b = 0
n = 0
outset = {}
with open('../1爬取关键词微博/temp.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        s = s + 1
        obj = int(line)
        if obj in tSet:
            t = t + 1
        else:
            if obj in outset:
                b = b + 1
            else:
                n = n + 1
                outset[obj] = 1

            
with open('待爬取用户微博ID表.txt', 'w', encoding='UTF-8') as out:
    for key in outset:
        out.write(str(key) + '\n')

print("过滤前" + str(s))
print("黑名单命中" + str(t))
print("重复" + str(b))
print("输出" + str(n))
print(str(s / n * 100) + '%')