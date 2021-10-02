T= int(input())
D=[]
E=[]
def circular_right_shift(value, n) :
	num_bits_in_int = 3
	n = n % num_bits_in_int
	mask = (1 << num_bits_in_int) - 1
	result = (value >> n) | (value << (num_bits_in_int - n))
	result = result & mask
	return result

def testcase():
	i=0
	C=[]
	A,B=map(int,input().split())
	while i<len(bin(max(A,B))):
		C.append(A^B)
		B=circular_right_shift(B,1)
		i=i+1
	D.append(C.index(max(C)))
	E.append(max(C))
for i in range(T):
	testcase()
for j in range(len(D)):
		print(D[j],end=' ')
		print(E[j])
