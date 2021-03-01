import os
import sys
sys.path.append(os.getcwd())

import pytest
import requests
from utils.dbtools import query
from utils.filetools import write_file,read_file
from utils.exceltools import read_excel
datas = read_excel(excel_path='data/测谈网v1.6接口.xlsx',sheet_name='个人中心')

def test_01_update_userinfo(): # 修改个人资料
    u = datas[0][2]
    h = eval(datas[0][3])
    d = eval(datas[0][4])
    
    res = requests.post(url=u,headers=h,json=d)
    print(res.text)
    assert res.status_code == datas[0][5]
    assert res.json()['status'] == datas[0][6]
    
    sql = "select * from t_user where nickname='{}' and phone='{}' and sex='{}' and email='{}'".format(d['nickname'],d['phone'],d['sex'],d['email'])
    assert len(query(sql)) !=0

def test_02_user_fell(): 
    # 点赞
    u = datas[1][2]
    h = eval(datas[1][3])
    d = eval(datas[1][4])
    
    res = requests.post(url=u,headers=h,json=d)
    print(res.text)
    assert res.status_code == datas[1][5]
    assert res.json()['status'] == datas[1][6]

    sql = "select * from t_questions_user_status where qid={} and gstatus={}".format(d['gid'],0)
    assert len(query(sql)) != 0

def test_03_user_fell(): 
    # 收藏
    u = datas[2][2]
    h = eval(datas[2][3])
    d = eval(datas[2][4])
    
    res = requests.post(url=u,headers=h,json=d)
    print(res.text)
    assert res.status_code == datas[2][5]
    assert res.json()['status'] == datas[2][6]

    sql = "select * from t_questions_user_status where qid={} and cstatus={}".format(d['cid'],0)
    assert len(query(sql)) != 0

def test_04_get_user_status():  
    #查看用户对于文章/灵感/问题等的关注、收藏、点赞的状态
    u = datas[3][2]
    h = eval(datas[3][3])
    d = eval(datas[3][4])
    
    res = requests.post(url=u,headers=h,json=d)
    print(res.text)
    assert res.status_code == datas[3][5]
    assert res.json()['status'] == datas[3][6]

    sql ="select * from t_questions_user_status where qid={} and gstatus={} and cstatus={}".format(d['fid'],res.json()['data'][0]['gstatus'],res.json()['data'][0]['cstatus'])
    assert len(query(sql)) != 0
   