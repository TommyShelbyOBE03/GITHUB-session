l = int(input())
a = []
sum  = 0
for i in range(l):
    a.append(int(input()))
for j in range(l):
    sum = sum + a[j]
print(sum)
