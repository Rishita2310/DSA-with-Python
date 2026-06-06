# How Many Numbers Are Smaller Than the Current Number
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            ans.append(count)
        
        return ans
    
print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))