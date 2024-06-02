# 将步骤封装成函数
def calculatePaperMoney(salary: int):
    hundred, salary = divmod(salary, 100)  # 解包赋值
    fifty, salary = divmod(salary, 50)
    twenty, salary = divmod(salary, 20)
    ten, salary = divmod(salary, 10)
    one, salary = divmod(salary, 1)
    return (hundred, fifty, twenty, ten, one)


print(calculatePaperMoney(salary=9853))