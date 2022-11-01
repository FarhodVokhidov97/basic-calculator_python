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
    answer = a^b
    print(str(a)+'^'+str(b)+'='+str(answer))

print("A, add(+)")
print("B, sub(-)")
print("C, nul(*)")
print("D, div(/)")
print("E, sqrt(^)")
choice = str(input('Input your choise'))
match choice:
    case "A":
        print("You can become a web developer.")

    case "B":
        print("You can become a Data Scientist")

    case "C":
        print("You can become a backend developer")
    
    case "D":
        print("You can become a Blockchain developer")

    case "E":
        print("You can become a mobile app developer")
    case _:
        print("letter must be Uppercase")