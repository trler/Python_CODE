# 完成收发工资案例
# 某公司 有1w元的余额,给20名员工发工资.
# 员工编号,从1到20,从编号1,开始,依次领取工资,每人可以领取1000元
# 领工资时,财务判断员工的绩效分1-10分,(随机生成),如果低于5,则不发工资,换下一位
# 如果工资领完了,结束发工资.
import random
whole_salary = 10000
for x in range(1,21):
    num = random.randint(1,10)
    if whole_salary == 0:
        print("工资全部发完,停止发工资")
        break
    else:
        if num < 5:
            print(f"{x}号员工绩效低于5,不发工资")
        else:
            whole_salary -= 1000
            print(f"{x}号员工绩效高于5,发工资1000元,公司余额{whole_salary}元")
print('工资发完了')