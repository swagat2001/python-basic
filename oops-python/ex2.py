class MATH_FUN():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def ADD(self):
        return(self.a+self.b)
    
    def MUL(self):
        return(self.a*self.b)
    
    def DIV(self):
        return(self.a/self.b)
    
    def SUB(self):
        return(self.a-self.b)

obj = MATH_FUN(100,10)
add = obj.ADD()
mul = obj.MUL()
sub = obj.SUB()
div = obj.DIV()
print(f'add:{add}')
print(f'mul:{mul}')
print(f'sub:{sub}')
print(f'div:{div}')