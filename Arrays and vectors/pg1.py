# Find maximum element from the given array of integers.
# Input Format

# First line of input contains N - the size of the array and second line contains the elements of the array.

# Constraints

# 1 <= N <= 100
# -109 <= ar[i] <= 109

# Output Format

# Print the maximum element of the given array.



N=int(input())
arr=list(map(int,input().split()))
m=max(arr)
print(m)
