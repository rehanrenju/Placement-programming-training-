
# Given an array on integers, search a given key in the array using linear search.
# Note: Do not use any inbuilt functions/libraries for your main logic.

# Input Format

# First line of input contains two integers, N - size of the array and K - search key. Second line contains the elements of the array.

# Constraints

# 1 <= N <= 102
# 0 <= ar[i] <= 109

# Output Format

# If key is found, print the index of the array, otherwise print -1.
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
N, K = map(int, input().split())
array = list(map(int, input().split()))
result = linear_search(array, K)
print(result)
