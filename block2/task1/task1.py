def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while (i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A
f = open("input.txt").readlines()
f = f[1].split()
a = []
for i in range(len(f)):
   a.append(int(f[i]))
insertionSort(a)
result = ' '.join(map(str, a))
o = open("output.txt", "w")
o.write(result)
o.close()