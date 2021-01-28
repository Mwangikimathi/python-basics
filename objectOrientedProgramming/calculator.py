name = "tech"
num = 1
class Calculator:
    

    def __init__(self, num1, num2):
       self.num1 = num1
       self.num2 = num2
    
    def get_sum(self):
        sum = (self.num1 + self.num2)
        return sum 

    def get_subtraction(self):
        subtraction = (self.num1 - self.num2)
        return subtraction 

    def get_multiplication(self):
        multiplication = (self.num1 * self.num2)
        return multiplication 

    def get_division(self):
        division = (self.num1 / self.num2)
        return division 
m1 = Calculator(-10, -10)
print(m1.get_sum())
print(m1.get_subtraction())
print(m1.get_multiplication())
print(m1.get_division())
