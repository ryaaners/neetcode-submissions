class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        left, right = 0, len(height) - 1
        lMax, rMax = height[left], height[right]
        while left < right:
            if lMax < rMax:
                left += 1
                lMax = max(lMax, height[left])
                res += lMax - height[left]
            else:
                right -= 1
                rMax = max(rMax, height[right])
                res += rMax - height[right]
        return res