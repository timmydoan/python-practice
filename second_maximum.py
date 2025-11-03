if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    nd_maximum = sorted(list(set(arr)))[-2]
    print(nd_maximum)
