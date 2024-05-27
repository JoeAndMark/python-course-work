num = input("请输入一个包含括号的表达式:")
stack = []
flag = 1

for i in num:
    if i == '(' or i == '[' or i == '{':
        stack.append(i)
    elif i == ']':
        if stack[-1] == '[':
            stack.pop(-1)
        else:
            flag = 0
            break
    elif i == '}':
        if stack[-1] == '{':
            stack.pop(-1)
        else:
            flag = 0
            break
    elif i == ')':
        if stack[-1] == '(':
            stack.pop(-1)
        else:
            flag = 0
            break

if len(stack) == 0 and flag == 1:
    print("匹配成功")
else:
    print("匹配失败")
