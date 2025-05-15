"""
和文件相关的类定义
"""
import json
from data_define import *
# 一个csv 一个 json 需要定义一个抽象类,子类具体实现两种功能
class File_Reader:

    def read_file(self) -> list[Record] :
        """ 将文件中的数据 都转换为record对象, 将他们都封装到list内返回即可"""
        pass

class textfile_reader(File_Reader):
    def __init__(self, path) -> None:
        self.path = path
    # 定义成员变量,记录文件路径

    def read_data(self) -> list[Record] :
    # 实现抽象方法
        f = open(self.path, 'r', encoding='utf-8')
        record_list : list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(',')
            record= Record(data_list[0], data_list[1], int(data_list[2]),data_list[3])
            record_list.append(record)

        return record_list
        # print(record_list)
        f.close()

class json_reader(File_Reader):
    def __init__(self, path) -> None:
        self.path = path

    def read_data(self) -> list[Record] :
        f = open(self.path, 'r', encoding='utf-8')
        record_list : list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict['money']), data_dict["province"])
            record_list.append(record)

        return record_list
        # print(record_list)
        f.close()


if __name__ == '__main__':
    txt = textfile_reader("2011年1月销售数据.txt")
    txt.read_data()
    json1 = json_reader("2011年2月销售数据JSON.txt")
    json1.read_data()