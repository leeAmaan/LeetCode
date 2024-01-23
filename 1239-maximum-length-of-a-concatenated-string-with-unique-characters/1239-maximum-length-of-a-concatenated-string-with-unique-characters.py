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
        # print(len(set(i)))
        # print(dp)
        # mid = []
        # for i in range(len(arr)-1):
        #     mid.append(arr[i]+arr[i+1])
        # res = []
        # print(mid)
        # dp[i]