# -*- coding: gbk -*-


import json
import re


# ��ȡ��Ų����������
def extract_number(file_name):
    # ƥ�������ֿ�ͷ����Ų��֣�����ƥ��༶��ţ��� "1.1", "2.3" �ȣ�
    match = re.match(r"(\d+(?:\.\d+)*)", file_name)
    if match:
        # �����ƥ���������ţ��򷵻�һ������Ԫ��
        return tuple(map(int, match.group(1).split('.')))
    else:
        # ���û����Ų��֣�����û�� "1.1" �����֣�������һ���ǳ����Ԫ��
        return (float('inf'),)  # ��û����ŵ��ļ��������


# ͨ������������߹�������ɸѡ https://pan.baidu.com/api/list? �����Ӧֵ�����浽 list.json ��

with open('./list.json', 'r', encoding='utf-8', errors='ignore') as f:
    data = f.read()
    data = json.loads(data)
    data_list = data['list']
    filename_list = []
    for i in data_list:
        filename_list.append(i['server_filename'])
    # �����ļ���
    sorted_list = sorted(filename_list, key=extract_number)
    for i in sorted_list:
        print(i.split('.mp4')[0])
