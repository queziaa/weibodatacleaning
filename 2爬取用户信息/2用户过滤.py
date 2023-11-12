# encoding=utf-8
import json

i = 0
s = 0
t = 0
digit_set = {}
foll = {}
with open('爬取用户信息过滤.txt', 'w', encoding='UTF-8') as outfile:
    with open('爬取用户信息合并.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            s = s + 1
            obj = json.loads(line)

            if(obj['verified']==True):
                continue
            if(obj['followers_count'] > 2000):
                continue
            if int(obj['statuses_count']) < 20:
                if int(obj['statuses_count']) in foll:
                    foll[int(obj['statuses_count'])] = foll[int(obj['statuses_count'])] + 1
                else:
                    foll[int(obj['statuses_count'])] = 1

            # print(obj['screen_name'])
            outfile.write(obj['_id'] + '\n')
            i = i + 1
print(foll)

print(i)
print(s)
print(t)
print(str(i / s * 100) + '%')

#
# K       foll
# 0      247726
# 1      13980
# 2      3893
# 3      1880
# 4      1270
# 5      1044
# 6      654
# 7      482
# 8      400
# 9      352
# 10	 709
# 11	 477
# 12	 324
# 13	 281
# 14	 227
# 15	 213
# 16	 173
# 17	 135
# 18	 120
# 19	 102
# 20	 168
# 21	 128
# 22	 119
