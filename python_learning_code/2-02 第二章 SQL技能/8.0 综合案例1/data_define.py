class Record: # 数据封装类
    # date = None
    # order_id = None
    # money = None
    # province = None
    # 或者直接构造方法进行定义
    def __init__(self,date,order_id,money,province):
        self.date = date  # 日期
        self.order_id = order_id # id
        self.money = money # 金额
        self.province = province # 省份

    def __str__(self):
        return f"record类对象,data={self.date},order_id = {self.order_id},money = {self.money}, provine = {self.province}"
    def __repr__(self):
        return str(self)
