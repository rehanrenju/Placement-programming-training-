#kjcjlksn
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
N, K = map(int, input().split())
array = list(map(int, input().split()))
result = linear_search(array, K)
print(result)
