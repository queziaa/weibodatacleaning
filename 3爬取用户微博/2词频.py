stop_words = set()
with open('baidu_stopwords', encoding='utf-8') as f:
    for line in f:
        stop_words.add(line.strip())

word_count = {}
with open('最终.txt', encoding="utf-8") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in stop_words:
                continue
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

# 根据count数值排序
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# 将结果存入文件
with open('词频.txt', 'w', encoding='utf-8') as f:
    for word, count in sorted_word_count:
        f.write(f'{word}: {count}\n')