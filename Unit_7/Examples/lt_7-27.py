import os


path = input("请输入文件路径:")
os.chdir(path)
print(os.getcwd())
filename = input("请输入文件名:")

if os.path.exists(filename):
    os.remove(filename)
    print("文件删除完毕")
else:
    print("文件不存在")