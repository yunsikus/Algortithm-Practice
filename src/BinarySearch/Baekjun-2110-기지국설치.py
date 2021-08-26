def is_possible(home,m,n,l): # home: 정렬된 집의 좌표, m: 최대거리를 m으로 가정, n: 설치해야할 공유기의 개수, l: 집의 개수
    cur_val = home[0]
    index = 1
    ip_count = 1
    while index <= l-1:
        if cur_val+m > home[index]:
            index += 1
            continue
        else:
            cur_val = home[index]
            ip_count += 1
            if ip_count == n:
                return True
            index += 1

    return False

def solution(home,n,l):
    lower = 0
    upper = 1000000000
    while lower <= upper:
        mid = (lower + upper) // 2
        if is_possible(home,mid,n,l): 
            lower = mid + 1
        else:
            upper = mid - 1
    return lower-1

if __name__ == "__main__":
    l, n = map(int, input().split())
    home = []
    for _ in range(l):
        home.append(int(input()))
    home.sort()
    print(solution(home,n,l))