# 函数如何返回多个返回值
def test_return():
    return 1, "hello",False
x, y ,z = test_return()
print(f"x={x}\ny={y}\nz={z}")
