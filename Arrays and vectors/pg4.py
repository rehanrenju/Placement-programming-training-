# Find a duplicate element in the given array of integers. There will be only a single duplicate element in the array.
# Note: Do not use any inbuilt functions/libraries for your main logic.

# Input Format

# First line of input contains size of the array - N and second line contains the elements of the array.

# Constraints

# 2 <= N <= 100
# 0 <= ar[i] <= 109

# Output Format

# Print the duplicate element from the given array.

#fdjlskn
N=int(input())
a=list(map(int,input().split()))
def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for i in arr:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)

    return list(duplicates)

duplicate_elements = find_duplicates(a)
for i in duplicate_elements:
    print(i)
