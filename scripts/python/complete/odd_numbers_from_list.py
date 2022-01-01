#!/usr/bin/env python3

def odd_list(N):
    L = []
    for i in range(0,N):
        if not i % 2 == 0:
            L.append(i)
    return L

def main():
    limit = 100
    result = odd_list(limit)  
    print(result)
    return

if __name__ == '__main__':
    main()
