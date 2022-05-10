from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            combs = [[first] + comb
                    for comb in combs
                    for first in range(1, comb[0] if comb else 10)]
        return [c for c in combs if sum(c) ==n]
        
        
        