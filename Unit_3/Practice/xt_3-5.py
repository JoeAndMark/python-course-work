class Solution:
    def __init__(self, salary):
       self.salary =  salary

    def calculate_tax(self) -> int:
        if 0 <= self.salary <= 3000:
            return 0
        elif 3000 < self.salary <= 5000:
            return self.salary * 0.02
        elif 5000 < self.salary <= 8000:
            return (self.salary - 5000) * 0.03
        elif self.salary > 8000:
            return (self.salary - 8000) * 0.04