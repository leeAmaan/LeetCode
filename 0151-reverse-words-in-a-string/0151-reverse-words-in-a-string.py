class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.split()
        a = strings[::-1]
        b = ' '.join(a)
        return b 