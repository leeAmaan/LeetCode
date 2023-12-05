class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        mid = n
        while mid > 1:
            print(mid)
            if mid%2 == 0:
                total_matches += (mid//2)
                mid = mid//2 
            else: 
                total_matches += ((mid-1)//2)
                mid = mid//2 + 1
        return total_matches 
