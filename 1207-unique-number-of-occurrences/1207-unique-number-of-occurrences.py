

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = Counter(arr)
        # print(arr)
        ans = []
        for i in arr.values():
            ans.append(i)
        # print(len(set(ans)))
        return len(set(ans)) == len(ans)    