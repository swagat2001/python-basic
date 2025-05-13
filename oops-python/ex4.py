class MATH_FUN():
    def ADD(self,a,b):    
        return(a+b) 

    def MUL(self,a,b):
        return(a*b)
    
add = MATH_FUN().ADD(10,20)
mul = MATH_FUN().MUL(10,20)
print(f'add:{add}')
print(f'mul:{mul}')