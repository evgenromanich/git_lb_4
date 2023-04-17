from random import*
N = 10
A = [randint(-10,10) for i in range (N)]
print(A)
for i in range(N):
	k = A[i]
	j = i -1
	while j >= 0 and k > A[j]:
		A[j+1] = A[j]
		j = j -1
	A[j+1] = k
print(A)
print("-------------------------------------------------")
N = 10
A = [randint(-10,10) for i in range (N)]
print(A)
for i in range(N-2, 0, -1):
	k = A[i]
	j = i + 1
	while j < N-1 and k > A[j]:
		A[j] = A[j+1]
		j = j - 1
	A[j-1] = k
print(A)
print("-------------------------------------------------")
N = 10
A = [randint(-10,10) for i in range (N)]
print(A)
min = A[0]
max=A[0]
for i in range(1, N):
	if A[i] < min : min = A[i]
	if A[i] > max : max = A[i]
M = max - min +1

X = [0]*M
for i in A:
	X[i-min] +=1
print(X)
j = N-1
for i in range(N,-1,-1):
	while X[i] != 0:
		A[j] = i + min
		j += 1
		X[i] -= 1
print(A)