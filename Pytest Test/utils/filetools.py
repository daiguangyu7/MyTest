

def write_file(filepath, content):
    """
        方法：文件写入
        参数：
            filepath：文件路径
            content： 要写入的内容
        返回值：None
    """

    with open(file=filepath, mode='w', encoding='utf-8') as f:
        f.write(str(content))


def read_file(filepath):
    """
        方法名：文件读取
        参数：
            filepath：文件路径
        返回值：返回文件的内容， 类型为str
    """
    with open(filepath, mode='r', encoding='utf-8') as f:
        result = f.readline()

    return result



# write_file('./tmp/test.txt', "张同学快了击剑速成宝典")

# print(read_file('./tmp/test.txt'))