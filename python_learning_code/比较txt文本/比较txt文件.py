# try:
#     # 读取第一个文件（f.txt）并提取数字
#     with open("export_uids (1).txt", "r", encoding="utf-8") as f:
#         content_f = f.read().strip()
#         numbers_f = set(content_f.split(','))  # 按逗号分割成集合
#
#     # 读取第二个文件（f1.txt）并提取数字
#     with open("export_uids.txt", "r", encoding="utf-8") as f1:
#         content_f1 = f1.read().strip()
#         numbers_f1 = set(content_f1.split(','))  # 按逗号分割成集合
#
#     # 找出f1中存在但f中没有的数字（去重逻辑：f1 - f）
#     unique_numbers = numbers_f1 - numbers_f1.intersection(numbers_f)
#
#     # 将结果写入新文件，保持原有逗号分隔格式
#     with open("unique_numbers.txt", "w", encoding="utf-8") as out_file:
#         if unique_numbers:
#             out_file.write(','.join(unique_numbers))  # 用逗号连接数字
#         else:
#             print("f1中没有多余的数字，无需输出。")
#
#     print(f"去重完成，已将f1中多出的{len(unique_numbers)}个数字保存到unique_numbers.txt")
#
# except FileNotFoundError as e:
#     print(f"错误：文件未找到 - {e.filename}")
# except Exception as e:
#     print(f"发生未知错误：{e}")


import pyperclip
import time


def read_numbers_from_file(file_path):
    """从文件读取数字字符串并返回列表"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            # 处理各种可能的分隔符：逗号、空格、换行等
            numbers = content.replace('\n', ',').replace(' ', ',').split(',')
            # 过滤掉空字符串并去除首尾空白
            return [num.strip() for num in numbers if num.strip()]
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return []


def main():
    # 提示用户输入文件路径
    file_path = input("请输入包含数字串的文件路径: ").strip()
    if not file_path:
        print("文件路径不能为空，程序退出。")
        return

    # 读取数字
    numbers = read_numbers_from_file(file_path)
    if not numbers:
        print("未找到有效的数字串，程序退出。")
        return

    print(f"找到 {len(numbers)} 个数字串")

    for i, num in enumerate(numbers, 1):
        try:
            # 复制到剪贴板
            pyperclip.copy(num)
            print(f"\n已复制第 {i}/{len(numbers)} 个数字串到剪贴板:")
            print(f"{num}")

            # 显示倒计时
            for j in range(3, 0, -1):
                print(f"\r即将自动继续，按Enter可提前确认... {j}", end='')
                time.sleep(1)
            print("\r按Enter继续下一个...", end='')

            # 等待用户按Enter
            input()

        except KeyboardInterrupt:
            print("\n程序被用户中断，退出。")
            break
        except Exception as e:
            print(f"\n处理数字串时出错: {e}")
            input("按Enter继续下一个...")


if __name__ == "__main__":
    print("数字串自动复制工具")
    print("=" * 30)
    main()