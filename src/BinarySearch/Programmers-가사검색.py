from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

data = [[] for x in range(10001)]
reversed_data = [[] for x in range(10001)]

def solution(words, queries):
    result = []
    for word in words:
        data[len(word)].append(word)
        reversed_data[len(word)].append(word[::-1])
        
    for i in range(10001):
        data[i].sort()
        reversed_data[i].sort()
        
    for query in queries:
        if query[0] != "?":
            answer = count_by_range(data[len(query)], query.replace('?','a'), query.replace('?','z'))
        else:
            answer = count_by_range(reversed_data[len(query)], query[::-1].replace('?','a'), query[::-1].replace('?','z'))
        result.append(answer)
    return result