class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a_sum = [nums[0]]
        max_v = nums[0]
        for i in range(1,len(nums)):
            hubo = max(nums[i], a_sum[-1]+nums[i])
            a_sum.append(hubo)
            if hubo > max_v:
                max_v = hubo
        return max_v