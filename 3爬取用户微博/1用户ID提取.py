# encoding=utf-8
import jieba
import json
import os
import re
import emoji
from urllib.parse import urlparse
import operator
from jieba import posseg as pseg

i = 0
s = 0
t = 0
idSet = {}
# srtset = {}
with open('有效用户ID.txt', 'w', encoding='UTF-8') as outfile:
    with open('爬取用户微博合并.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            s = s + 1
            obj = json.loads(line)
            parsed_url = urlparse(obj['url'])
            p_id = parsed_url.path.split('/')[1]
            p_id = int(p_id)
            if p_id in idSet:
                idSet[p_id] += 1
            else:
                idSet[p_id] = 1

    print(len(idSet))
    sorted_srtset = sorted(idSet.items(), key=operator.itemgetter(1), reverse=True)
    print(len(sorted_srtset))
    i = 0

    numSet = {}
    idSet2 = {}
    for k in sorted_srtset:
        # if k[1] in numSet:
        #     numSet[k[1]] += 1
        # else:
        #     numSet[k[1]] = 1
        if k[1] >= 4:
            outfile.write(str(k[0]) + '\n')
    # i += 1
    # print(sorted_srtset[i-1])
    # print(i)
# for k in numSet:
#     print(k, numSet[k])
