from collections import deque

def solution(prices):
    queue = deque([[0, prices[0]]])
    answer = [0] * len(prices)
    for i in range(1, len(prices)):
        for pos, price in queue:
            answer[pos] += 1
        while queue and queue[-1][1] > prices[i]:
            queue.pop()

        queue.append([i, prices[i]])

    return answer
