class Solution:
    def __init__(self, total_yield):
        self.total_yield = total_yield
        self.top_3_of_yield = sorted(self.total_yield.keys(), key=lambda k: self.total_yield[k], reverse=True)[:3]

    def __str__(self):
        return f"The top 3 sorted by yield are {self.top_3_of_yield}\nThe rate of top 3 is {self.calculate_rate() * 100:.2f}%"

    def calculate_rate(self):
        total_of_yield = sum(self.total_yield.values())
        total_of_top_3 = sum(self.total_yield[province] for province in self.top_3_of_yield)
        return total_of_top_3 / total_of_yield
