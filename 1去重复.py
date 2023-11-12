import json

idset = {}
with open('2爬取用户信息/爬取用户信息合并去重.txt', 'w', encoding='UTF-8') as output:
    with open('2爬取用户信息/爬取用户信息合并.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            obj = json.loads(line)
            if obj['_id'] not in idset:
                idset[obj['_id']] = 1
                output.write(line)
            else:
                print(obj)

            