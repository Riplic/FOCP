def someFunc(x, y, z):
	print("x is", x, "\ny is", y, "\nz is", z)

someFunc(y=2, z=3, x=1)

#calling the function in several different orders.
someFunc(z=3, x=1, y=2)
someFunc(x=1, y=2, z=3)
