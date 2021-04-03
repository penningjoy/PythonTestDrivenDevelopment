class addition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @classmethod
    def additioner(cls, a, b):
        if(a is not None  and b is not None):
            return cls(a,b)
        else:
            return None

    def summation(self):
        return self.num1 + self.num2
