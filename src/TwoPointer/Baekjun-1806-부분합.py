N,S = map(int, input().split())
my_list = list(map(int, input().split()))

min_len = 1000001
start = 0
end = 1

cumsum = [0]*(len(my_list)+1)
for i in range(1, len(my_list)+1):
    cumsum[i] = cumsum[i-1] + my_list[i-1]

while start < N:
    my_s = cumsum[end]-cumsum[start]
    if my_s >= S:
        min_len = min(min_len, end-start)
        start += 1
    else:
        if end < N:
            end += 1
        else:
            start += 1

if min_len == 1000001:
    print(0)
else:
    print(min_len)