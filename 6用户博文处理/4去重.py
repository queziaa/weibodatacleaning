# 打开并读取第一个文件，将每行保存在一个集合中
with open('用户ID.txt', 'r') as f:
    completed_tasks = {line.strip() for line in f}

# 打开并读取第二个文件，将每行保存在另一个集合中
with open('../1爬取关键词微博/neg.txt', 'r') as f:
    all_tasks = {line.strip() for line in f}

# 使用集合的差集操作来找出未完成的任务ID
unfinished_tasks = all_tasks - completed_tasks

# 打开一个新的文件，并将未完成的任务ID写入到这个文件中
with open('未完成ID.txt', 'w') as f:
    for task in unfinished_tasks:
        f.write(task + '\n')