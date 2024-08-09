# Print array in reverse order.
# Note: Try solving this using recursion. Do not use any inbuilt functions/libraries for your main logic.

# Input Format

# First line of input contains N - the size of the array and second line contains the elements of the array.

# Constraints

# 1 <= N <= 100
# 0 <= ar[i] <= 1018

# Output Format

# Print the given array in reverse order.
N=int(input())
a=list(map(int,input().split()))
def reverse_list_recursive(lst, start, end):
    # Base case: when start index crosses end index
    if start < end:
        # Swap the elements at start and end indices
        lst[start], lst[end] = lst[end], lst[start]
        
        # Recursive call on the rest of the list
        reverse_list_recursive(lst, start + 1, end - 1)

reverse_list_recursive(a, 0, len(a) - 1)
for i in a:
  print(i,end=" ")
