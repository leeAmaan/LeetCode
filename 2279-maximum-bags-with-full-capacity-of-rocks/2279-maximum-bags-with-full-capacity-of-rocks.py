class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # print(starmap(sub, zip(capacity, rocks)))
        return bisect_right(list(accumulate(sorted(starmap(sub, zip(capacity, rocks))))), additionalRocks) 
    
    
    """ max_cap = sum(rocks) + additionalRocks
        ans = 0
        prefix = list(accumulate(sorted(capacity))) 
        #rocks.sort()
        print(prefix)
        for i in range(len(prefix)):
            if (max_cap - prefix[i]) < 0:
                return ans 
            else: 
                ans +=1
        return ans"""