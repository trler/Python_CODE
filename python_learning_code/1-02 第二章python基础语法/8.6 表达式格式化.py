# 了解什么是表达式
# 掌握对表达式进行字符串格式化

# 表达式：一条具有明确执行结果的代码语句

# 1+1 5*2 就是表达式，因为有具体的结果，结果是一个数字

print("1*1的结果是 : %d"% (1*1))
print(f"1*2的结果是 : {1*2}")
print("字符串在python中的数据类型为: %s "% type("字符串"))

# 作业
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor =   1.2
growth_days = 7
print(f"公司名{name},当前股价{stock_price},股票代码{stock_code}")
print(f"每日增长系数为:{stock_price_daily_growth_factor},经过{growth_days}天后,股票变成了%.2f" % (stock_price*stock_price_daily_growth_factor**growth_days))