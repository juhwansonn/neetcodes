class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for i in range(26):
            if count[i] != 0:
                return False 
        
        return True 

        # time complexity - O(n) where n is the length of s and m
        #                   return false if they are not the same len 
        # space complexity - O(1) 
