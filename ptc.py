n, k = map(int, input().split())
L = list()
for i in range(k):
    L.append(map(float, input().split()))
for i in zip(*L):
    print(sum(i)/k)