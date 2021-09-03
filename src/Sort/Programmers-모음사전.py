from bisect import bisect_left
from itertools import product

def index_of_x(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None

def solution(word):
    alpha_list =[''.join(list(j)) for i in range(1,6) for j in product(['A','E','I','O','U'], repeat=i)]    
    alpha_list.sort()
    
    return index_of_x(alpha_list,word) + 1