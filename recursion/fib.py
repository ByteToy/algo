def fib_recursion(n):
    if n<=1:
        return n
    else:
        return fib_recursion(n-1)+fib_recursion(n-2)


if __name__=="__main__":
    for i in range(1,31):
        print(i,fib_recursion(i))