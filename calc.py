from cmath import sqrt
from multiprocessing.connection import answer_challenge
from secrets import choice


def add(a, b):
    answer = a + b
    print(str(a)+'+'+str(b)+'='+str(answer))

def sub(a,b):
    answer = a-b
    print(str(a)+'-'+str(b)+'='+str(answer))

def mul(a,b):
    answer = a*b
    print(str(a)+'*'+str(b)+'='+str(answer))
    
def div(a,b):
    answer = a/b
    print(str(a)+'/'+str(b)+'='+str(answer))
    

def square(a,b):
    answer = pow(a,b)
    print(str(a)+'^'+str(b)+'='+str(answer))

print("A, add(+)")
print("B, sub(-)")
print("C, mul(*)")
print("D, div(/)")
print("E, sqrt(^)")
choice = str(input('Input your choise'))
match choice:
    case "A":
        a= int(input('input a='))
        b= int(input('input b='))
        add(a,b)

    case "B":
        a= int(input('input a='))
        b= int(input('input b='))
        sub(a,b)

    case "C":
        a= int(input('input a='))
        b= int(input('input b='))
        mul(a,b)
    
    case "D":
        a= int(input('input a='))
        b= int(input('input b='))
        div(a,b)

    case "E":
        a= int(input('input a='))
        b= int(input('input b='))
        square(a,b)
    case _:
        print("letter must be Uppercase")