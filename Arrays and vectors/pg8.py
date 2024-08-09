def find_repeating_numbers(arr):
    # Dictionary to keep track of occurrences of each number
    freq = {}
    duplicates = []
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num, count in freq.items():
        if count == 2:
            duplicates.append(num)
    
    return sorted(duplicates)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + N]))
        index += N
        
        result = find_repeating_numbers(arr)
        results.append(" ".join(map(str, result)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
