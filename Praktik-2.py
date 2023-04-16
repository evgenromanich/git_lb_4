def creat(N,M,x = 0):
	A = [0]*N
	for i in range(N):
		A[i] = [x]*M
	return A

def input_matr(A):
	N = len(A)
	if N == 0:
		N = int(input("Введите количесво строк в матрице "))
	for i in range (N):
		print("Введите элемениы %d-ой строки в одну строку" %i)
		st = list (input().split())
		A[i] = list(map(int(), st))
	return A

def print_matr (A):
	for i in range (len(A)):
		for j in range (len(A[i])):
			print (A[i][j], end= ' ')
		print()

A = input_matr
print_matr(A)
#-----------------------------------------

def stat(A):
	B = creat_matr(len(A),3,0)
	for i in range (len(A)):
		for j in range(len(A[i])):
			print("%4d" % A[i][j])
		print()

def stat(A):
	B = creat_matr(len(A),3,0)
	for i in range (len(A[i])):
		B[i][j] = A[i][0]
		B[i][1] = A[i][0]
		B[i][2] = A[i][0]


	for j in range (1, len(A[i])):
		B[i][j] = A[i][0]
		B[i][1] = A[i][0]
		B[i][2] = A[i][0]



A = input_matr
print_matr(A)
B = stat(A)