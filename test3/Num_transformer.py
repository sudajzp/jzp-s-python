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
            for j in range(3):
                if self.num >= num_list[i]:
                    roman_list.append(str_list[i])
                    self.num -= num_list[i]
        return ''.join(roman_list)

def judge_num(n):
    while True:
        if n.isdigit():
            n = int(n)
            return n
        else:
            n = input('请输入有效的正整数:')
            return judge_num(n)

if __name__ == '__main__':
    n = input('请输入您想要查找的数字：')
    num = Number(judge_num(n))
    roman = num.transform()
    print(roman)