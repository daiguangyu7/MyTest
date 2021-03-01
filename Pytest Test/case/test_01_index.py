"""首页模块"""
import os
import sys
sys.path.append(os.getcwd())

import pytest
import requests
from utils.exceltools import read_excel

datas = read_excel(excel_path='data/测谈网v1.6接口.xlsx',sheet_name='首页')

def test_01_lbt():
    # 轮播图
    u = datas[0][2]
    res = requests.get(url = u)

    assert res.status_code == datas[0][5]
    assert res.json()['status'] == datas[0][6]

def test_02_tjjc():
    # 获取推荐教程
    u = datas[1][2]
    res = requests.get(url = u)

    assert res.status_code == datas[1][5]
    assert res.json()['status'] == datas[1][6]

def test_03_get_questions():
    # 讨论区
    u = datas[2][2]
    res = requests.get(url = u)

    assert res.status_code == datas[2][5]
    assert res.json()['status'] == datas[2][6]

def test_04_get_articles():
    # 获取热门文章
    u = datas[3][2]
    res = requests.get(url = u)

    assert res.status_code == datas[3][5]
    assert res.json()['status'] == datas[3][6]

def test_05_get_inspirers():
    # 获取灵感
    u = datas[4][2]
    res = requests.get(url = u)

    assert res.status_code == datas[4][5]
    assert res.json()['status'] == datas[4][6]

def test_06_get_users():
    # 获取活跃用户
    u = datas[5][2]
    res = requests.get(url = u)

    assert res.status_code == datas[5][5]
    assert res.json()['status'] == datas[5][6]

def test_07_tag_list():
    # 获取标签
    u = datas[6][2]
    h = eval(datas[6][3])
    
    res = requests.get(url=u,headers=h)
    assert res.status_code == datas[6][5]
    assert res.json()['status'] == datas[6][6]

def test_08_search():
    # 搜索文章
    u = datas[7][2]
    h = eval(datas[7][3])
    
    res = requests.get(url=u,headers=h)
    assert res.status_code == datas[7][5]
    assert res.json()['status'] == datas[7][6]