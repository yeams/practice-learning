# 将字符串倒序输出
s = "123456789"
print(s[::-1]) # a[i:j:s] s<0时，i缺省默认为-1. j缺省默认为-len(a)-1，s表示步进
# 交换x,y两个变量的值
x = 2
y = 3
x = x^y
y = x^y
x = x^y
# a,b = b,a
print(x,y)

# 下面代码第6行的赋值顺序
def fib(n):
	 """Compute the nth Fibonacci number, for n >= 2."""
	pred, curr = 0, 1   # Fibonacci numbers 1 and 2
	k = 2               # Which Fib number is curr?
	while k < n:
		pred, curr = curr, pred + curr
		k = k + 1
	return curr
	
result = fib(8)

pred = 0, 1, 1, 2, 3, 5, 8
curr = 1, 1, 2, 3, 5, 8, 13
