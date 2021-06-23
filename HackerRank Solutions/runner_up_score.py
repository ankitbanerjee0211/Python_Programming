if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    winner = max(arr)
    for i in range(n):
        if winner in arr:
            arr.remove(winner)
    runner_up = max(arr)
    print(runner_up)