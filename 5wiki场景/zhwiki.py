# encoding=utf-8
# from calendar import c
# from itertools import count
# import jiagu
from calendar import c
import jieba
# import json
# import os
import re
# import emoji
# from urllib.parse import urlparse
from jieba import posseg as pseg
import time
from regex import W
# from torch import le, manager_path
import zhconv
# from snownlp import SnowNLP

# from regex import P

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
title = ''
miantext = ''
Category = ''
with open('wiki-out.txt', 'w', encoding='UTF-8') as outfile:
    with open('zhwiki-20231101-pages-articles-multistream_1.xml', 'r', encoding='UTF-8') as f:
        for line in f:
            s = s + 1

            # 输出跳过内容
            # if cont == 1:
            #     print('----------------------------------')
            #     print(obj['content'])
            # cont = 1
            content = line.strip()
            content = content.replace(' ', '')
            if content == '':
                continue
            content = zhconv.convert(content, 'zh-cn')
            c0 = content[0]
            if c0 == '<':
                if content.find('<title>') != -1:
                    if len(miantext) > 30 and title.find('Wikipedia') == -1 and len(Category) > 0:
                        outfile.write(title + '\n')
                        outfile.write(Category + '\n')
                        outfile.write(miantext + '\n')
                        outfile.write('----------------------------------\n')
                    miantext = ''
                    Category = ''
                    content = content.replace('<title>', '')
                    content = content.replace('</title>', '')
                    title = content
                continue
            if c0 == '|':
                continue
            if c0 == '[':
                if content.find('[[Category') != -1:
                    content = re.sub(r'[a-zA-Z\W]+', '', content)  # 删除英文和符号
                    Category = Category + content + ' '
                continue
            if c0 == '{':
                continue
            if c0 == '&':
                continue  
            if c0 == '=':
                content = content.replace('=', '')
                if content in ['参考文献','注解','来源','参见','相关页面','引用','注释','外部链接','脚注','其他资源']:
                    continue
            words = pseg.lcut(content)
            words = [word for word, flag in words if flag in ['n', 'nr', 'ns', 'nz', 'ng', 'nrt', 'nt', 'nrfg']]
            if len(words) ==    0:
                continue
            for word in words:
                if word in digit_set:
                    digit_set[word] = digit_set[word] + 1
                else:
                    digit_set[word] = 1

            miantext = miantext + ' '.join(words)

            i = i + 1
            if s % 10000 == 0:
                print(str(s / 213602158 * 100)[:5], '%', str(i / s * 100)[:5] + '%')

print(i)
print(s)
sorted_digit_set = sorted(digit_set.items(), key=lambda x: x[1], reverse=True)
with open('key-out.txt', 'w', encoding='UTF-8') as outfile:
    for k, v in sorted_digit_set.items():
        outfile.write(k + ' ' + str(v) + '\n')

end_time = time.time()  # 记录结束时间
print(f"处理{s}条博文共耗时{end_time - start_time:.2f}秒")  # 打印时间统计结果