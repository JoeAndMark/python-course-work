def avg(lst):
    return int(sum(lst) / len(lst))

s = {
    "小李": [77, 54],
    '小张': [89, 66, 78, 99],
    '小陈': [90],
    '小杨': [69, 58, 93]
}

ss = {}

for k, v in s.items():
    