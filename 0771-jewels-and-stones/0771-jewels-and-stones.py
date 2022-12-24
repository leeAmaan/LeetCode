class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0
        
        # 비교 없이 돌 빈도 수 계산
        for char in stones:
            freqs[char] += 1
        #print(freqs)
        # 비교 없이 보석 빈도 수 합산
        for char in jewels:
            count += freqs[char]
        
        return count
        #return sum(s in jewels for s in stones)
        
        