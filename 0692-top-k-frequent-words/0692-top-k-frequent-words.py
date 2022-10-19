from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = Counter(words)
        ans = sorted(ans, key=lambda word:(-ans[word], word)) 
        #list(ans.keys())
        print(ans)
        res = []
        
        for i in range(k):
            res.append(ans[i])
        
        
        return res