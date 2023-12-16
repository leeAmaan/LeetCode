class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # print(sorted(list(s)))
        # print(sorted(list(t)))
        if sorted(list(s)) == sorted(list(t)):
            return True 
        else: 
            return False