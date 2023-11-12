# # encoding=utf-8
# from calendar import c
# import fontTools
# import jieba
# import json
# import os
# import re
# import emoji
# from urllib.parse import urlparse
# import operator
# from jieba import posseg as pseg
# from regex import P
#
# i = 0
# s = 0
# idSet = {}
#
# with open('关键词微博.txt', 'w', encoding='UTF-8') as outfile:
#     with open('爬取用户微博合并.txt', 'r', encoding='UTF-8') as f: #125W
#         for line in f:
#             s = s + 1
#             obj = json.loads(line)
#             parsed_url = urlparse(obj['url'])
#             p_id = parsed_url.path.split('/')[1]
#             p_id = int(p_id)
#             if p_id not in idSet:
#                 idSet[p_id] = 1
#             else:
#                 idSet[p_id] += 1
#
#             if p_id not in idSet:
#                 idSet[p_id] = {}
#             content = obj['content']
#             ###################################
#             content = re.sub(r'@[\w]+', '', content)
#             content = re.sub(r'(\w)\1{2,}', '', content)
#             content = re.sub(r'\[[^\]]{1,6}\]', '', content)
#             content = content.lower()
#             ###################################
#             # n
#             # nr 不明
#             # nz 相对 细化 专业的名词
#             # ng 单字
#             # nrt 音译名字 误差大
#             # nt 团体组织
#             # nrfg 人名
#             # nz 其它专名*
#             # ns 地名和位置
#             if content.find('hiv') != -1 or content.find('艾滋') != -1 or content.find('恐艾') != -1:
#                 outfile.write(str(p_id) + ' ' + content + '\n')
#
#
#
# print(i)
# print(s)
# print(str(i / s * 100)[0:4] + '%')
#
