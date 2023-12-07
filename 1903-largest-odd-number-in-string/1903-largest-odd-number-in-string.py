class Solution:
    def largestOddNumber(self, num: str) -> str:
        return num[:next((i for i in range(len(num)-1, -1, -1) if ord(num[i]) &1==1), -1) + 1]