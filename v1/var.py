import os

# 打开文件
with open('var.txt', 'r') as file:
    # 逐行读取文件内容
    line = file.readline()

    # 循环直到文件末尾
    while line:
        # 处理当前行
        # print(line.strip())  # 使用strip()去除行末尾的换行符
        file_name = os.path.basename(line)
        target_string = file_name.split('.')[0]  # 假设目标字符串是文件名的第一部分，以点号分隔
        print(target_string)
        # l = ["message(STATUS \"", target_string, ": ${", target_string, "}\")"]
        # s = "".join(l)
        # print(s)

        # 读取下一行
        line = file.readline()

