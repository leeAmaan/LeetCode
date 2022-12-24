class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #print()
        return sum(s in jewels for s in list(stones))
        #return sum(s in jewels for s in stones)
        
        