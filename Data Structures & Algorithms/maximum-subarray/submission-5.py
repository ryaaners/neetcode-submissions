class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        maxSum = float('-inf')
        curSum = 0

        for i in nums:
            curSum += i
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0

                
        return maxSum