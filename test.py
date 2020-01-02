

def Fibonacci(n):
    output = [None]*1000
    output[0],output[1] = 0,1
    
    result = output[n]
    if result == None:
        result = Fibonacci(n-1) + Fibonacci(n-2)
        output[n] = result
    return result

n = int(input('请输入要计算第几项斐波那契数列：'))

for i in range(n+1):
    print('Fibonacci(%d)=%d' %(i,Fibonacci(i)))