'''
- constant memory
- runtime is at worst time to traverse first string + time to traverse second string

racecar
carrace

- can have counts stored in some array since at most you will ever collect counts for 26 letters where as strings can be really long
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = dict()

        for char in s:
            if char in char_count:
                char_count[char]+=1
            else:
                char_count[char] = 1

        for char in t:
            if char in char_count:
                char_count[char] -= 1
            else:
                return False
        
        if any(value != 0 for value in char_count.values()):
            return False
        else:
            return True
        


        
        