def is_possible(n, times, hubo):
    total = 0
    for time in times:
        total += (hubo // time)
    if total >= n:
        return True
    else: 
        return False

def solution(n, times):
    lower, upper, mid = 0, times[-1]*n, 0
    while lower <= upper:
        mid = (lower+upper) //2
        if is_possible(n, times, mid):
            upper = mid - 1
        else:
            lower = mid + 1
    return upper + 1
