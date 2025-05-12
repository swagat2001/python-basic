class MATH_FUN():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def ADD(self):
        return(self.a+self.b)

    def MUL(self):
        add=self.ADD()
        print(f'add:{add}')
        return(self.a*self.b)
mul = MATH_FUN(100,200).MUL()
print(f'mul:{mul}') 