import os

# 定义目录路径
folder_path = '../../用户博文/'

# 遍历目录下的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # 删除文件
        os.remove(file_path)