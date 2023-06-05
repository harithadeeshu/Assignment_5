#2: Implement a Calculator Class

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        print(self.num2 + self.num1)

    def subtract(self):
        print(self.num2 - self.num1)

    def multiply(self):
        print(self.num2 * self.num1)

    def divide(self):
        print(self.num2 / self.num1)

cal = Calculator(10, 94)
cal.add()
cal.subtract()
cal.multiply()
cal.divide()