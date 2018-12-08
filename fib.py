#斐波那契数列
#第一个值为1，第二个值也为1，第三个值是2，后面的值等于前两个值之和
#公式f(n)=f(n-1)+f(n-2)
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)

#调用
print(fib(5))