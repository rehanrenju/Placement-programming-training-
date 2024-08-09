11.0 / 11.0
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
