import json
import os
import re
# encoding=utf-8
import jieba
import json
import os
import re
import emoji
from urllib.parse import urlparse
import operator
from jieba import posseg as pseg


directory = '../../用户博文/'
idSet = {}

with open('用户ID.txt', 'w', encoding='UTF-8') as outfile:
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件扩展名是否为.jsonl
        if filename.endswith('.jsonl'):
            with open(os.path.join(directory, filename), 'r', encoding="utf-8") as f:
                for line in f:
                    print(line)
                    obj = json.loads(line)
                    parsed_url = urlparse(obj['url'])
                    p_id = parsed_url.path.split('/')[1]
                    p_id = int(p_id)
                    if p_id in idSet:
                        idSet[p_id] += 1
                    else:
                        idSet[p_id] = 1
                    break
    for key in idSet:
        outfile.write(str(key) + '\n')