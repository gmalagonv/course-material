ops = {"+": "add",
       "-": "sub",
       "*": "mul",
       "/": "truediv",
       }
number = input("number")
a = number.split("(")
print(a)
b= a[1].split(")")#a[0]= first Num, b[0]=operator, b[1]=second num
print(b)
try:
    int(a[0]), int(b[1])
except ValueError:
    print("input error")
else:
    if b[0] in ops:
        print("ok")
    else:
        print("input error")
        
    
    
        