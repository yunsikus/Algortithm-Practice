import collections
def isPalindrome(self, head: ListNode) -> bool:
    q: Deque = collections.deque()

    if not head:
        return True
    
    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next
    
    # 펠린드롬 판별
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
          
    return True