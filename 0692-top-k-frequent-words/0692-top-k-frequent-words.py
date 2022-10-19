from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = Counter(words)
        ans = sorted(ans, key=lambda word:(-ans[word], word)) 
        return ans[:k]
   