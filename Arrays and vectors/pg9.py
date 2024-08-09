def main():
    n = int(input().strip())
    columns = list(map(int, input().strip().split()))
    columns.sort()
    print(" ".join(map(str, columns)))
if __name__ == "__main__":
    main()
