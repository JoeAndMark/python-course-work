class Solution:
    def __init__(self, *revenue):
        # class list
        # self.revenue = list(revenue)
        # list comprehension
        # self.revenue = [i for i in revenue]
        # loop
        self.revenue = []
        for i in revenue:
            self.revenue.append(i)
        self.weekday = sum(self.revenue[0:6:1])
        self.weekend = sum(self.revenue[6::1])

    def __str__(self):
        print_str = (f'The total of Revenue during weekdays is {self.weekday}\n'
                     f'The total of Revenue during weekends is {self.weekend}\n'
                     f'And the Difference between Weekdays and Weekends is {self.calculate_difference()}')
        return print_str

    def calculate_difference(self):
        return abs(self.weekday - self.weekend)
