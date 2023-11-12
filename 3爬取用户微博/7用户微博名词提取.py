# encoding=utf-8
import fontTools
import jieba
import json
import os
import re
import emoji
from urllib.parse import urlparse
import operator
from jieba import posseg as pseg
from regex import P

i = 0
s = 0
idSet = {}

with open('名词用户对应.txt', 'w', encoding='UTF-8') as outfile:
    with open('爬取用户微博合并.txt', 'r', encoding='UTF-8') as f: #125W
        for line in f:
            s = s + 1
            obj = json.loads(line)
            parsed_url = urlparse(obj['url'])
            p_id = parsed_url.path.split('/')[1]
            p_id = int(p_id)
            if p_id not in idSet:
                idSet[p_id] = {}
            content = obj['content']
            ###################################
            content = re.sub(r'@[\w]+', '', content)
            content = re.sub(r'(\w)\1{2,}', '', content)
            content = re.sub(r'\[[^\]]{1,6}\]', '', content)
            ###################################
            # n
            # nr 不明
            # nz 相对 细化 专业的名词
            # ng 单字
            # nrt 音译名字 误差大
            # nt 团体组织
            # nrfg 人名
            # nz 其它专名*
            # ns 地名和位置
            i += 1
            words = pseg.lcut(content)
            for word, flag in words:
                if flag in ['n', 'nr', 'ns', 'nz', 'ng', 'nrt', 'nt', 'nrfg']:
                    if word in idSet[p_id]:
                        idSet[p_id][word] = idSet[p_id][word] + 1
                    else:
                        idSet[p_id][word] = 1
            if s % 10000 == 0:
                print(s/1250000*100)

    out = {}
    for key, value in idSet.items():
        out[key] = sorted(idSet[key].items(), key=lambda x: x[1], reverse=True)

    for key, value in out.items():
        outfile.write('{' + str(key) + ',' + str(value) + '}\n')


print(i)
print(s)
print(str(i / s * 100)[0:4] + '%')

