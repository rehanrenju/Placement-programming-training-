# You are given an array of N elements. All elements of the array are in range 1 to N-2. All elements occur once except two numbers, which occur twice. Your task is to find the two repeating numbers.

# Input Format

# First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array and second line contains the elements of the array.

# Constraints

# 30 points
# 1 <= T <= 100
# 4 <= N <= 103

# 70 points
# 1 <= T <= 100
# 4 <= N <= 106

# Output Format

# Print the 2 repeated numbers in sorted manner, for each test case, separated by new line.
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
