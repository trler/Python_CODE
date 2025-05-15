# 1.掌握使用while循环,遍历列表的元素
# 2.掌握使用for循环,遍历列表的元素
from idlelib.debugobj import myrepr


# def list_while_func():
#     """
#     利用while循环来遍历list的演示函数
#     :return:
#     """
#     my_list = ["传智教育","黑马程序员","Python"]
#     index = 0;
#     while index < len(my_list):
#         print(my_list[index])
#         index += 1
# def list_for_func():
#     """
#     利用for循环来遍历list的演示函数
#     :return: None
#     """
#     my_list = ["船只加u","黑马程序员","Python"]
#     index = 0;
#     for index in range(len(my_list)):
#         print(my_list[index])
#         index += 1
#     # for循环新用法
#     for i in my_list:
#         print(i)
# list_for_func()
# list_while_func()

# 依次取出并操作叫做遍历,while for循环进行遍历
#

# 作业 取出列表中的偶数 遍历列表,取出偶数,存入新链表,使用while for各操作依次
list = [1,2,3,4,5,6,7,8,9,10]
def list_operation_while(data):
    index = 0
    list_2 = []
    while index < len(data):
        if data[index]%2 == 0:

            list_2.append(data[index])
            index += 1
        else:
            index += 1
    return list_2
def list_operation_for(data):
    count = 0
    list_2 = []
    for index in data:
        if index%2 == 0:
            count += 1
            list_2.append(index)
    return list_2

print(list_operation_while(list))
print(list_operation_while(list))

