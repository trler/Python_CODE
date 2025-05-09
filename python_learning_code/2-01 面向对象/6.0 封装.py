# 面向对象编程的三大套路 封装 继承 多态
# 封装

# 私有成员使用 对用户隐藏的属性和行为
# 类中提供了私有成员的形式和方法
# 私有成员变量, 私有成员方法  定义是时候 __开头就可以

# 私有方法 无法被 类对象调用使用
# 私有变量 也无法被赋值 无法获取值

# 定义一个有私有方法属性的类

# class Phone:
#
#     __current_voltage = 0.1
#     def __keep_single_core(self):
#         print("单核模式")
#
#     def call_by_5g(self):
#         if self.__current_voltage >= 1:
#             print("开挖掘机")
#         else:
#             self.__keep_single_core()
#             print("电量不足,无法使用挖掘机,已经为您自动设置自爆环节")
#
#
# apple = Phone()
# # apple.__keep_single_core()
# # print("apple.__current_voltage") # 均无法使用
#
# # 虽然无法被对象使用, 但是可以 被其他内部成员使用 手机拍照要检测电压温度
#
# apple.call_by_5g()


# 作业 设计5g功能开启显示的手机

class phone:
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable == True : ## .self.属性 忘记改了
            print("5g已经开启")
        else:
            print("5g关闭,使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")
## 忘记创建对象
ph = phone()
ph.call_by_5g()

