# 直接调用write,内容并未真正写入文件,而是会积攒在利程序的内存中,称之为缓冲区
# 当调用flush的时候,内容会真正写入文件
# 这样做是避免频繁的操作硬盘,导致效率下降(攒一堆,一次性写磁盘)

import time
f = open("test.txt","w",encoding="utf-8")

# write 写入
f.write("hello world\n"
        "我人杀了\n"
        "此时此刻我")
time.sleep(3)
f.flush() # 刷新后将内容写入

# 关闭
f.close() # 内置flush功能



