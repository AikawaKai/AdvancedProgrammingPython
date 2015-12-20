def fibric(a,b,n):
	if n == 1 :
		return b
	else:	
		c = a + b
		n -= 1
		return fibric(b,c,n)


def fib(n) :
	if n == 0:
		return None
	else:
		a=0
		b=1
		return fibric(a,b,n)

def fibric1(n):
	return 0 if n == 0  else (1 if n <= 2 else fibric1(n-1)+fibric1(n-2))



if __name__ == '__main__':
	for i in range(0,101) :
		print('Fib {0:3d} = {1}'.format(i,fib(i)))
	for i in range(0,101) :
		print('Fib1 {0:3d} = {1}'.format(i,fibric1(i)))
