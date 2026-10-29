from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)
        left, right = 0, 0
        while right < len(s2):
            if s2[right] in counts and counts[s2[right]] > 0:
                counts[s2[right]] -= 1
                right += 1
                if sum(counts.values()) == 0:
                    return True
            else:
                counts = Counter(s1)
                left += 1
                right = left
        return False