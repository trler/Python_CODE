# 文件操作模块, file_util.py
    # print_file_info(file.name) 接受传入文件路径,打印文件全部内容,如果文件不存在则捕获异常,输出提示信息,通过finally关闭文件对象
    # append_to_file(file.name,data),接受文件路径传入数据,将数据追加到文件中
__all__=["print_file_info","append_to_file"]
def print_file_info(file_info):
    f = None
    try:
        f = open(file_info, 'r',encoding='utf-8')
        for line in f:
            print(line)
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()

def append_to_file(file_info,data):
    f = None
    f = open(file_info, 'a',encoding='utf-8')
    f.write(data)
    f.close()