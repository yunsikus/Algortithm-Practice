# 1. Hashmap
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_set = set()
        for n in nums: # O(N)
            if n in my_set:
                my_set.discard(n)
            else:
                my_set.add(n)
        return list(my_set)[0]
    
# 2. XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums: 
            result ^= n
        return result