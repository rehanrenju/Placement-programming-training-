#kjndlksjfv
N = int(input())
array = list(map(int, input().split()))
element_counts = {}
for num in array:
    element_counts[num] = element_counts.get(num, 0) + 1
for num in array:
    if element_counts[num] == 1:
        print(num,end=" ")
        element_counts[num] = 0
