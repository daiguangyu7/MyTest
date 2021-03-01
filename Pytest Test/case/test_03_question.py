import os
import sys
sys.path.append(os.getcwd())

import pytest
import requests
from utils.dbtools import query
from utils.filetools import write_file,read_file
from utils.exceltools import read_excel

datas = read_excel(excel_path='data/测谈网v1.6接口.xlsx',sheet_name='问题')
def test_01_new_question():
    # 新建问题
    u = datas[0][2]
    h = eval(datas[0][3])
    d = eval(datas[0][4])

    res = requests.post(url=u,headers=h,json=d)
    assert res.status_code == datas[0][5]
    assert res.json()['status'] == datas[0][6]
    
    write_file('./tmp/questionid.txt',res.json()['data']['questionid'])
    questionid = read_file('./tmp/questionid.txt')
   
    sql = "select * from t_questions where id={} and title='{}' and content='{}' and tags='{}' and brief='{}' and ximg='{}'".format(questionid,d['title'],d['content'],d['tags'],d['brief'],d['ximg'])
    assert len(query(sql)) != 0

def test_02_get_question():
    # 获取问题详情
    questionid = read_file('./tmp/questionid.txt')
    u = datas[1][2]
    h = eval(datas[1][3])
    p = eval(datas[1][4])
    res = requests.get(url=u,headers=h,params=p)
    assert res.status_code == datas[1][5]
    assert res.json()['status'] == datas[1][6]

def test_03_comment_new():
    # 新建评论
    u = datas[2][2]
    h = eval(datas[2][3])
    d = eval(datas[2][4])

    res = requests.post(url=u,headers=h,json=d)
    assert res.status_code == datas[2][5]
    assert res.json()['status'] == datas[2][6]
    #print(res.text)
    
    sql = "select * from t_user_comments where ctype='{}' and comment='{}' and fid={}".format(d['ctype'],d['comment'],d['fid'])
    assert len(query(sql)) != 0

def test_04_get_comments():
    # 获取评论列表
    u = datas[3][2]
    h = eval(datas[3][3])
    d = eval(datas[3][4]) #文章类型，0教程1提问2灵感3心得体会

    res = requests.post(url=u,headers=h,json=d)
    assert res.status_code == datas[3][5]
    assert res.json()['status'] == datas[3][6]

    write_file('./tmp/question_comment_id.txt',res.json()['data']['contentlist'][0]['id'])
    #print(res.text)

def test_05_comment_update():
    # 修改评论
    u = datas[4][2]
    h = eval(datas[4][3])
    d = eval(datas[4][4])

    res = requests.post(url=u,headers=h,json=d)
    assert res.status_code == datas[4][5]
    assert res.json()['status'] == datas[4][6]

    sql = "select * from t_user_comments where id={} and comment='{}'".format(read_file('./tmp/question_comment_id.txt'),d['comment'])
    assert len(query(sql)) != 0
    #print(res.text)

def test_06_comment_delete():
    # 删除评论
    u = datas[5][2]
    h = eval(datas[5][3])
    d = eval(datas[5][4]) 

    res = requests.post(url=u,headers=h,json=d)
    assert res.status_code == datas[5][5]
    assert res.json()['status'] == datas[5][6]

    sql = "select * from t_user_comments where id={} and status='1'".format(read_file('./tmp/question_comment_id.txt'))
    assert len(query(sql)) != 0