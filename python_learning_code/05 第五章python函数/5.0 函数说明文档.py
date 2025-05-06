# 1.掌握通过注释对函数进行解释说明

def function(x,y):
    """
    函数定义为x的y次方
    :param x: 底数
    :param y: 指数
    :return: 返回结果
    """
    if y == 1:
        return x
    else:
        for i in range(2,y+1):
            x *=x
            i +=1
        return x
print(function(3, 2))