import json
import os
import re

directory = '../../用户博文/'


# 遍历目录中的所有文件
for filename in os.listdir(directory):
    # 检查文件扩展名是否为.jsonl
    if filename.endswith('.log'):
        # 打开并读取文件
        statuscode = {}
        with open(os.path.join(directory, filename), 'r', encoding="utf-8") as f:
            for line in f:
                if line.find('''response_status_count''') != -1:
                    line = line.replace('downloader/response_status_count/', '')
                    line = line.replace(':', 'A')
                    line = re.sub(r'\W+', '', line)
                    s = line.split('A')
                    statuscode[s[0]] = s[1]

        for key in statuscode:
            if len(statuscode) == 0:
                print(filename)
                break
            if '200' == key:
                if statuscode[key] == 1:
                    print(filename)
                    break
            elif key in '414':
                print(filename)
                break
            elif key in ['500','302','400','502']:
                if '200' in statuscode:
                    if int(statuscode['200']) / int(statuscode[key]) < 10:
                        print(filename)
                        break
                else:
                    print(filename)
                    break
            else:
                print('-----------------')
                print(filename)
                print('-----------------')
                break