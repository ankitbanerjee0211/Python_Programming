a = input().split()
n = int(a[0])
m = int(a[1])
c = '-'
d = '.|.'

for i in range(n//2):
    center = int(i*2 + 1)
    dash = int((m - 3*center)/2)
    print(c*dash+ d*center+ c*dash)
sides = int((m-7)/2)
print(c*sides + 'WELCOME' + c*sides)
for j in range(n//2):
    center2 = int(n - 2 - 2*j)
    dash2 = int((m - 3*center2)/2)
    print(c*dash2+ d*center2+ c*dash2)
