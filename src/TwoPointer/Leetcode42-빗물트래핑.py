def trap(self, height: List[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right] # 3, 2

    while left < right:
        # 왼쪽, 오른쪽 최대값 갱신
        left_max, right_max = max(heights[left], left_max), max(heights[right], right_max)
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - heights[left]
            left += 1
        else:
            volume += righ_max - heights[right]
            right -= 1
    return volume