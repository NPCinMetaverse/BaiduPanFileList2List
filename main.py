# -*- coding: gbk -*-


import json
import re


# 提取序号并按序号排序
def extract_number(file_name):
    # 匹配以数字开头的序号部分，可以匹配多级序号（如 "1.1", "2.3" 等）
    match = re.match(r"(\d+(?:\.\d+)*)", file_name)
    if match:
        # 如果有匹配的数字序号，则返回一个数字元组
        return tuple(map(int, match.group(1).split('.')))
    else:
        # 如果没有序号部分（例如没有 "1.1" 等数字），返回一个非常大的元组
        return (float('inf'),)  # 将没有序号的文件排在最后


# 通过浏览器开发者工具网络筛选 https://pan.baidu.com/api/list? 获得响应值，保存到 list.json 中

with open('./list.json', 'r', encoding='utf-8', errors='ignore') as f:
    data = f.read()
    data = json.loads(data)
    data_list = data['list']
    filename_list = []
    for i in data_list:
        filename_list.append(i['server_filename'])
    # 排序文件名
    sorted_list = sorted(filename_list, key=extract_number)
    for i in sorted_list:
        print(i.split('.mp4')[0])
