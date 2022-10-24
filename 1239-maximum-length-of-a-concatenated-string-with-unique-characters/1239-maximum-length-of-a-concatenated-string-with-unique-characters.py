class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for i in arr:
            if len(set(i)) < len(i):
                continue
            i = set(i)
            for j in dp[:]:
                if i & j:
                    continue
                dp.append(i|j)
        return max(len(i) for i in dp)