import xlrd


def read_excel(excel_path, sheet_name, skip_first=True):
    """
        方法：
            python读取excel
        参数：
            excel_path：excel的路径
            sheet_name：首页/登录
            skip_first：是否跳过首行，True：跳过；False：不跳过

        返回值：
            [[1，测试轮播图功能正常， "http://xxxx",...], [2, 测试xxx, ..]]
    """
    results = []
    
    datas =  xlrd.open_workbook(excel_path) # 打开并且获取excel的操作对象/句柄/把柄
    table = datas.sheet_by_name(sheet_name) # 根据sheetname获取table页面的操作把柄
    if skip_first == True:
        start_row = 1
    else:
        start_row = 0
    
    # 循环读取excel的每一行数据: 固定就好
    for row in range(start_row, table.nrows):   # 指定要读取的下标
        results.append(table.row_values(row))

    return results

if __name__ == "__main__":
    excel = "data/测谈网v1.6接口.xlsx"
    a = read_excel(excel_path=excel, sheet_name="问题")
    print(a)
