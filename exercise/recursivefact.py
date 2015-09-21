
def fact(x) :
	return 1 if x == 1 else x * fact(x-1)

if __name__ == '__main__' :
	for i in [1, 2, 3, 4, 5, 6, 7, 15, 25, 30, 42, 100]:
		print('Fattoriale di {0:3d} = {1}'.format(i,fact(i)))