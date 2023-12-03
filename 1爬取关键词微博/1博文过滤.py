# encoding=utf-8
from calendar import c
from itertools import count

# import jiagu
# import jieba
import json
from operator import le
import os
import re
import emoji
from urllib.parse import urlparse
import time
import zhconv
from snownlp import SnowNLP

from regex import P

i = 0
s = 0
t = 0
cont = 0
digit_set = {}
# obj = {}
idList = {}
outid = {}
# foll = {}
start_time = time.time()  # 记录开始时间
# with open('../2爬取用户信息/爬取用户信息过滤.txt', 'r', encoding='UTF-8') as f:
#     for line in f:
#         if int(line) not in idList:
#             idList[int(line)] = 1

with open('temp.txt', 'w', encoding='UTF-8') as outfile:
    with open('../3爬取用户微博/爬取用户微博合并.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            s = s + 1

            # 输出跳过内容
            # if cont == 1:
            #     print('----------------------------------')
            #     print(obj['content'])
            # cont = 1

            obj = json.loads(line)
            content = obj['content']
            # id = int(obj['user']['_id'])
            # 筛选
            if len(content) > 200:
                continue
            # if id not in idList:
                # continue
            if content[0] == '【':
                continue
            if obj['source'] == '微博视频号':
                continue
            if obj['source'] == '微博发布平台专业版':
                continue
            # if 'video' in obj:
            #     continue
            content = content.lower()
            if content.find('http:') != -1:
                continue
            if content.find('https:') != -1:
                continue
            content = content.replace('hiv', '艾滋')
            content = content.replace('gay', '男同性恋')
            content = zhconv.convert(content, 'zh-cn')
            content = re.sub(r'\[[^\]]{1,6}\]', '', content)
            content = emoji.demojize(content)
            content = content.lstrip('啊哈')
            content = re.sub(r'@[\w]+', '', content)
            if len(re.findall(r'#[^#]*#', content)) > 6:  # 3720
                continue
            # content = re.sub(r'#[^#]*#', '', content) #删除井号包围的标题
            sub = ''
            if content.find('//') != -1:
                sub = content.split('//')[0]
                sub = re.sub(r'[a-zA-Z\W]+', '', sub)  # 删除英文和符号
            else:
                sub = re.sub(r'[a-zA-Z\W]+', '', content)  # 删除英文和符号
            sub = re.sub(r'[^\u4e00-\u9fa5\d]+', '', sub)
            if len(sub) < 2:
                continue
            if sub in ['转发微博', '转发', '艾滋', '呼吁2030年终结艾滋病']:
                continue
            content.replace(" ", "")
            content = re.sub(r'(\w)\1{2,}', '', content)
            content = re.sub(r'[^\u4e00-\u9fa5\d]+', '', content)
            if not 20 < len(content) < 30 :
                continue
            # if content.find('疫情') != -1:
            #     continue
            # if content.find('新冠') != -1:
            #     continue
            # if content.find('冠状病毒') != -1:
            #     continue
            # if content.find('日报') != -1:
            #     continue
            # sss = jiagu.seg(content)
            # sss = ' '.join(sss)

            # if id not in outid:
                # outid[id] = 1
            # else:
                # outid[id] = outid[id] + 1

            # sss = jiagu.sentiment(content)
            # n = sss[1]
            # if sss[0] == 'negative':
                # n = -n
            # n = n * 100
            # n = int(n)
            # if -66 > n:
                # if id not in outid:
                #     outid[id] = 1
                # else:
                #     outid[id] = outid[id] + 1


                # outfile.write(str(n) + '\n')
                # outfile.write(obj['content'] + '\n')
                # outfile.write('----------------' + '\n')

            # print(content)
            # print(sss)
            # print('--------------')
            # outfile.write(str(n) + '\n')
            outfile.write(content + '\n')

            # outfile.write(json.dumps(obj, ensure_ascii=False) + '\n')
            i = i + 1
            if s % 10000 == 0:
                print(str(s / 778000 * 100)[:5], '%', str(i / s * 100)[:5] + '%')
    for i in outid:
        outfile.write(str(i) + '\n')
print(i)
print(s)

end_time = time.time()  # 记录结束时间
print(f"处理{s}条博文共耗时{end_time - start_time:.2f}秒")  # 打印时间统计结果

#  len(content)/100
# 0	111369
# 1	35503
# 2	8595
# 3	4452
# 4	2837
# 5	1850
# 6	1274
# 7	782
# 8	506
# 9	583
