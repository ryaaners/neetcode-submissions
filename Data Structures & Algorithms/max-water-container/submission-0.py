class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater = 0
        length = len(heights)
        # started by initizilating our maximum water, 
        
        left, right = 0, length - 1
        #create pointers at first and last index

        while left < right:
            lowest = min(heights[left], heights[right])
            length = right - left
            #just variables to make our lives easier

            if lowest * length > maxwater:
                maxwater = lowest * length
            #setting our maximum amount of water

            if lowest == heights[left]:
                left += 1
            else:
                right -= 1
            #here it is important to use else or even elif here becuase
            #min return the leftmost value if both are equal
            #so this would just move our left pointer vs if we used
            #another if for the right pointer it could potentially
            #increase and decrease left and right in the same pass

        return maxwater