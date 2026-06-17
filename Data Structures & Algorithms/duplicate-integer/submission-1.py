'''
nums is int array

if any value in nums appears more than once in nums return true, otherwise false


'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        
        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)
        
        return False
