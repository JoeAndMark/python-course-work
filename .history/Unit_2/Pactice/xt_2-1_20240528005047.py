# 一种简单的贪心算法
# 思路一：使用多次整除和取余运算
# salary = 9853
# hundred = salary // 100
# salary %= 100
# fifty = salary // 50
# salary %= 50
# twenty = salary // 20
# salary %= 20
# ten = salary // 10;
# salary %= 10
# one = salary
# print(hundred, fifty, twenty, ten, one, end='\n')

# 思路二：使用 divmod(x, y) 函数
# salary = 9853
# hundred, salary = divmod(salary, 100)  # 解包赋值
# fifty, salary = divmod(salary, 50)
# twenty, salary = divmod(salary, 20)
# ten, salary = divmod(salary, 10)
# one, salary = divmod(salary, 1)
# print(hundred, fifty, twenty, ten, one)

# 将步骤封装成函数
def calculatePaperMoney(salary: int):
    hundred, salary = divmod(salary, 100)  # 解包赋值
    fifty, salary = divmod(salary, 50)
    twenty, salary = divmod(salary, 20)
    ten, salary = divmod(salary, 10)
    one, salary = divmod(salary, 1)
    return (hundred, fifty, twenty, ten, one)


print(calculatePaperMoney(salary=9853))

# from collections import namedtuple
# def calculate_paper_money(salary: int) -> namedtuple:
#     if not isinstance(salary, int) or salary < 0:
#         raise ValueError("Salary must be a non-negative integer.")
#     denominations = [100, 50, 20, 10, 1]
#     counts = []
#     for d in denominations:
#         count, salary = divmod(salary, d)
#         counts.append(count)
#     PaperMoney = namedtuple('PaperMoney', ['hundred', 'fifty', 'twenty', 'ten', 'one'])
#     return PaperMoney(*counts)
#
# print(calculate_paper_money(9853))