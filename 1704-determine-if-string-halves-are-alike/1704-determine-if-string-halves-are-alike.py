class Solution:
    def halvesAreAlike(self, s):
        s, n, cand = s.lower(), len(s), set("aeiou")
        return sum(i in cand for i in s[:n//2]) == sum(i in cand for i in s[n//2:])