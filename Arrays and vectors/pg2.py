#kjfcdf
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
