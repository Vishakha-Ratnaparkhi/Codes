#factorial
def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num-1)

def factorial_iterative(num):
    if num ==0 or num ==1:
        return 1
    res=1
    for i in range(2,num+1):
        res = res*i

    return res

num=int(input("enter num"))
n=factorial(num)
n2=factorial_iterative(num)
print(n)
print(n2)
