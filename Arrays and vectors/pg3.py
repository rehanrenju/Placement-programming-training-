N=int(input())
arr=list(map(int,input().split()))
odd_sum=0
for i in arr:
  if i%2 != 0:
    odd_sum+=i
print(odd_sum)
