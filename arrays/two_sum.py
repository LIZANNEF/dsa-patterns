#Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target.
from typing import List
class Solutions:
    def twoSum(self, nums : List[int], target: int) -> List[int]:
        seen = {}

        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num]=i
            
a = Solutions()
print(a.twoSum([1,2,3,4,2,4],4))
