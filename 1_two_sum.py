class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        step1: arrays are not sorted. so probably run through all elements
        step2:Initialize a dictionary. enumerate function is nice. it can keep track of index and value.
        so we take a value and track it and save it in a list. then move to the next items for remaining value
        
        """
        seen = {} # this is an empty list but this will store the balues checked so far.
        for i,value in enumerate(nums):
            remaining = target-nums[i]
            if remaining in seen:
                return [i,seen[remaining]]
            else:
                seen[value] = i