import os

# 读取文件内容
with open('11111111111111.csv', 'r') as f:
    lines = f.readlines()

size = 10000


num_files = len(lines) // size + 1
for i in range(num_files):
    start = i * size
    end = (i + 1) * size
    file_lines = lines[start:end]
    if not file_lines:
        break
    file_name = f'works{i+1}.txt'
    with open(file_name, 'w') as f:
        f.writelines(file_lines)
    print(f'Saved {file_name}')

print('Done')