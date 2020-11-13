#coding utf-8
'''
阿拉伯数字转罗马数字
'''
class Number():
    def __init__(self, num):
        self.num = num

    def transform(self):
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        str_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_list = []
        for i in range(len(num_list)):
            while self.num >= num_list[i]:
                roman_list.append(str_list[i])
                self.num -= num_list[i]
        print(''.join(roman_list))

if __name__ == '__main__':
    n = input('请输入您想要查找的数字：')
    if n.isdigit():
        n = int(n)      # 将输入化为整数型
        num = Number(n)
        num.transform()
    else:
        print('请输入有效的正整数')