if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max(arr) - min(arr))
