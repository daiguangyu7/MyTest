import os
import sys
sys.path.append(os.getcwd())

import pytest
import requests
from utils.dbtools import query
from utils.filetools import write_file,read_file
from utils.exceltools import read_excel
datas = read_excel(excel_path='data/测谈网v1.6接口.xlsx',sheet_name='用户')

def test_01_get_usrinfo():
    # 获取用户信息
    u = datas[0][2]
    h = eval(datas[0][3])
    res = requests.get(url = u,headers=h)

    assert res.status_code == datas[0][5]
    assert res.json()['status'] == datas[0][6]

def test_02_get_usrdt():
    # 获取用户动态
    u = datas[1][2]
    h = eval(datas[1][3])
    res = requests.get(url = u,headers=h)

    assert res.status_code == datas[1][5]
    assert res.json()['status'] == datas[1][6]

def test_03_getuserfstatus():
    # 获取用户是否被关注
    u = datas[2][2]
    h = eval(datas[2][3])
    
    res = requests.get(url = u,headers=h)
    # print(res.text)
    assert res.status_code == datas[2][5]
    assert res.json()['status'] == datas[2][6]

def test_04_userquestions():
    # 获取用户提问列表
    u = datas[3][2]
    h = eval(datas[3][3])
    res = requests.get(url = u,headers=h)

    assert res.status_code == datas[3][5]
    assert res.json()['status'] == datas[3][6]

def test_05_userfuser():
    # 用户关注用户
    u = datas[4][2]
    h = eval(datas[4][3])

    res = requests.get(url = u,headers=h)
    # print(res.text)
    assert res.status_code == datas[4][5]
    assert res.json()['status'] == datas[4][6]

    sql = "select * from t_user_follows where fid=322 and status=0"
    assert len(query(sql)) != 0