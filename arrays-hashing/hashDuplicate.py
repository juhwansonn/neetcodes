class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False 

    # Takes O(n) time complexity looping through all the elements 
    # in the input list 
    
    # Takes O(n) space complexity store all the numbers in the set. 
