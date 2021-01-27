import time

# Inisialisasi int, array, dan string
frek = -1
k = 0
z = int
a = []
A = ['*' for i in range(12)]
H = ['*' for i in range(1)]
n = "0123456789"
N = []
S = []

Puzzle = False

# Input
while (A[frek] != '------'):
    frek = frek + 1
    A[frek] = input()
H[0] = input()

start_time = time.time()

# Mengisi array huruf unik
for i in range(frek-1):
    for j in A[i]:
        if j not in S:
            S.append(j)
for y in A[frek-1]:
    if y not in S:
        if y != "+":
            S.append(y)
for k in range(len(H[0])):
    for l in H[0]:
        if l not in S:
            S.append(l)

# Inisialisasi array untuk menampung nilai array S
Angka_S = [0 for i in range(len(S))]

# Print Input, Array Char Unik, Array Angka
print(A)
print(S)
print(list(n))

# Fungsi Permutasi

def toString(List):
    return ''.join(List)

def permute(a, l, r, N):
    if l==r:
        N.append(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, N)
            a[l], a[i] = a[i], a[l] # backtrack

permute(list(n),0,len(n)-1, N)

# Fungsi untuk mencari nilai dari string di A
def Result(List1, List2, List3):
    x = int
    sum = 0
    for i in range(len(List1)):
        for j in range(len(List1[i])):
            for k in range(len(List2)):
                if List2[k] == List1[i][j]:
                    x = (10**(len(List1[i]) - j - 1))*List3[k]
                    sum += x
    return(sum)


for i in range(len(N)):
     for j in range(len(S)):
            Angka_S[j] = int(N[i][j])
            In = Result(A, S, Angka_S)
            Out = Result(H, S, Angka_S)
            if In == Out:
                Puzzle = True
                break

if Puzzle == True:
    print(In)


