# 文件备份案例
f1 = open("bill.txt","r",encoding="utf-8")
f2 = open("bill.txt.bak","w",encoding="utf-8")
for line in f1:
    num = line.count("正式")
    if num != 1:
        continue
    else :
        f2.write(line)
        f2.flush()
f1.close()
f2.close()
