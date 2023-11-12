import os

# 获取当前目录下所有以 .json 结尾的文件名
file_names = [f.name for f in os.scandir('.') if f.is_file() and f.name.endswith('.jsonl')]

# 打开目标文件
with open('爬取关键词微博.txt', 'w', encoding='UTF-8') as outfile:
    # 遍历所有文件并逐行写入目标文件
    for fname in file_names:
        with open(fname, encoding='UTF-8') as infile:
            for line in infile:
                outfile.write(line)


