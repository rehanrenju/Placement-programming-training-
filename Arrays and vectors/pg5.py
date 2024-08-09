# Print unique elements of the array in the same order as they appear in the input.
# Note: Do not use any inbuilt functions/libraries for your main logic.

# Input Format

# First line of input contains a single integer N - the size of array and second line contains array elements.

# Constraints

# 1 <= N <= 100
# 0 <= ar[i] <= 109

# Output Format

# Print unique elements of the array.


N = int(input())
array = list(map(int, input().split()))
element_counts = {}
for num in array:
    element_counts[num] = element_counts.get(num, 0) + 1
for num in array:
    if element_counts[num] == 1:
        print(num,end=" ")
        element_counts[num] = 0
