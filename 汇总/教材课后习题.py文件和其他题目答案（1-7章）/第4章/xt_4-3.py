class Solution:
    def __init__(self, my_str):
        self.my_str = my_str

    def my_split(self, sep: str) -> list:
        returnList = []
        i = j = 0
        for char in self.my_str:
            if char == sep:
                break