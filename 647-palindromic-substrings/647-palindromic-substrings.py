class Solution:
    def countSubstrings(self, s: str) -> int:
        @lru_cache(None)
        def isPalindrome(left, right):
            if left > right:
                return True
            if s[left] != s[right]:
                return False
            return isPalindrome(left+1, right-1)
        
        n = len(s)
        cnt = 0 
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):
                    cnt += 1
                
        return cnt