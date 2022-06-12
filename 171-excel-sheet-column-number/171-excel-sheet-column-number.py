class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum([(ord(T)-ord("A")+1)*26**i for i, T in enumerate(columnTitle[::-1])])