# 黑马atm
balance = 5000000
def menu():
    """
    主菜单
    :return:输入的数字
    """
    print("---------------主菜单----------------")
    print("周杰伦,您好,欢迎来到黑马银行ATM,请选择操作:")
    print("查询余额 \t[输入1]")
    print("存款     \t[输入2]")
    print("取款     \t[输入3]")
    print("退出     \t[输入4]")
    return int(input("请输入你的选择"))
def check_balance():
    print("---------------查询余额----------------")
    print(f"周杰伦,您好,您的余额剩余:{balance}元")
    print(f"您是否需要存取款服务呢?")
    print("存款     \t[输入2]")
    print("取款     \t[输入3]")
    print("退出     \t[输入4]")
    return int(input("请输入你的选择"))
def save_money(data):
    global balance
    balance += data
    print("---------------存款----------------")
    print(f"周杰伦,您好,您存款成功{data}元,现在余额{balance}元")
def withdraw_money(data):
    global balance
    balance -= data
    print("---------------取款----------------")
    print(f"周杰伦,您好,您取款成功{data}元,现在余额{balance}元")

while True:
    num = menu()
    if num == 1:
        num = check_balance()
    














    #     num = check_balance()
    #     if num == 2:
    #         money = int(input("您想存多少钱"))
    #         save_money(money)
    #     elif num == 3:
    #         money = int(input("您想存多少钱"))
    #         withdraw_money(money)
    #     elif num == 4:
    #         print("欢迎您的使用")
    #         break
    #     else:
    #         print("输入错误,请重新输入")
    # elif num == 2:
    #     money = int(input("您想存多少钱"))
    #     save_money(money)
    # elif num == 3:
    #     money = int(input("您想存多少钱"))
    #     withdraw_money(money)
    # elif num == 4:
    #     print("欢迎您的使用")
    #     break
    # else :
    #     print("输入错误,请重新输入")

