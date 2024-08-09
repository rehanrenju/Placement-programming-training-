#kjsf
t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    count=0
    for i in lis:
        count+=i
    print(count)
