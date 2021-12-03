def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums.sort()
    left, right = 0, len(nums)-1
    while not left == right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return left, right

def threeSum(self, nums: List[int], target: int) -> List[int]:
    results = []
    nums.sort()
    for i in range(len(nums)-2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 간격을 좁혀가며 합 sum계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                # sum = target인 경우에는 정답 및 스킵처리
                reuslts.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                # 그 다음부터 다시 시작
                left += 1
                right -= 1
    return results