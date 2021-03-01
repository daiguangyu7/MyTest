# 登陆模块
import os
import sys
sys.path.append(os.getcwd())

import pytest
import requests
from utils.dbtools import query
from utils.filetools import write_file,read_file
from utils.exceltools import read_excel

datas = read_excel(excel_path='data/测谈网v1.6接口.xlsx',sheet_name='登录')
def test_01_login_success():
    # 登录成功
    u = datas[0][2]
    h = eval(datas[0][3])
    d = eval(datas[0][4])

    res = requests.post(url=u,headers=h,json=d)
    assert res.status_code == 200
    assert res.json()['status'] == 200
    # 数据库校验
    sql = "select * from t_user where username = '{}'".format(d['username'])
    assert len(query(sql))

    write_file('./tmp/token.txt',res.json()['data']['token'])

def test_02_login_fail():
    u = 'http://118.24.255.132:2333/login'
    h = {"Content-Type":"application/json"}
    d = { "username":"daiguang","password":"a1234567"}

    res = requests.post(url=u,headers=h,json=d)
    assert res.status_code == 200
    assert res.json()['status'] != 200
