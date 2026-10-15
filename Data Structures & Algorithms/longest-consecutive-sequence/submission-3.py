class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numbers = set(nums)
        LCS = 1
        for n in numbers:
            i = n + 1
            count = 1
            if (n - 1) in numbers:
                continue
            while i in numbers:
                count += 1
                if count > LCS:
                    LCS = count
                i += 1
        return LCS