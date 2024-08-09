# Print sum of all odd elements in an array.

# Input Format

# First line of input contains N - the size of the array and second line contains array elements.

# Constraints

# 1 <= N <= 100
# -109 <= ar[i] <= 109

# Output Format

# Print sum of all odd elements of the given array.
N=int(input())
arr=list(map(int,input().split()))
odd_sum=0
for i in arr:
  if i%2 != 0:
    odd_sum+=i
print(odd_sum)
