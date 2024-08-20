"""
FDS Assignment-3

Que. Write a Python program to compute following computation on matrix:
a) Addition of two Matrices
B) Subtraction of two Matrices 
c) Multiplication of two Matrices 
d) Transpose of a Matrix 
"""

m=int(input(("Enter the Number of Rows: ")))
n=int(input(("Enter the Number of Columns: ")))

matrix1=[]
matrix2=[]
add=[]
diff=[]
multiplication=[]

#Matrix A
print("Enter elements of first matrix:")
for i in range(0,m):
	a=[]
	for j in range (0,n):
		a.append(int(input()))
	matrix1.append(a)
	
#Printing the matrix
print("Matrix A:")
for i in range(0,m):
	for j in range (0,n):
		print(matrix1[i][j], end=" ")
		if (j == n - 1):
		 	print("\n")
#Matrix B
print("Enter elements of second matrix:")	 	
for i in range(0,m):
	b=[]
	for j in range (0,n):
		b.append(int(input()))
	matrix2.append(b)

#Printing the matrix	
print("Matrix B:")
for i in range(0,m):
	for j in range (0,n):
		print(matrix2[i][j], end=" ")
		if (j == n - 1):
		 	print("\n")
		 		 	
def Add():
	print("\nAddition of two Matrices: \n")
	for i in range (0,m):
		c=[]
		for j in range (0,n):
			c = matrix1[i][j] + matrix2[i][j]
			print(c, end=" ")
		print("\n")
		add.append(c)
		
def sub():
	print("\nSubtraction of two Matrices: \n")
	for i in range (0,m):
		d=[]
		for j in range (0,n):
			d = matrix1[i][j] - matrix2[i][j]
			print(d, end=" ")
		print("\n")
		diff.append(d)
						
def multi():
	print("\nMultiplication of two Matrices: \n")
	p=[]
	for i in range (0,m):
		p.append([])
		#p=[i][j]
		for j in range (0,n):
			sum=0
			for k in range (0,n):
				sum = sum + (matrix1[i][k] * matrix2[k][j])
				p[i].append(sum)
			print(p[i][j], end=" ")
		print("\n")
								
def trans():
	print("Transpose of Matrix A:\n")
	r=[]
	for i in range (0,m):
		r.append([])
		for j in range (0,n):
			h=matrix1[j][i]
			r[i].append(h)
			print(r[i][j], end=" ")
		print("\n")

	
Add()
sub()
multi()
trans()


"""
Output

Enter the Number of Rows: 3
Enter the Number of Columns: 3
Enter elements of first matrix:
1
2
3
4
5
6
7
8
9
Matrix A:
1 2 3

4 5 6

7 8 9

Enter elements of second matrix:
9
8
7
6
5
4
3
2
1
Matrix B:
9 8 7

6 5 4

3 2 1


Addition of two Matrices:

10 10 10

10 10 10

10 10 10


Subtraction of two Matrices:

-8 -6 -4

-2 0 2

4 6 8


Multiplication of two Matrices:

9 21 30

36 66 84

63 111 138


Transpose of Matrix A:

1 4 7

2 5 8

3 6 9

"""


