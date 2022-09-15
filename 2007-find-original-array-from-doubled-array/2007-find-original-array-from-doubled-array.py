class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt = collections.Counter(changed)
        #print(sorted(cnt))
        if cnt[0] % 2:
            return []
        
        for i in sorted(cnt):
            if cnt[i] > cnt[2 * i]:
                return []
            cnt[2 * i] -= cnt[i] if i else cnt[i] // 2
        return list(cnt.elements())
        
        
        
        
        #res = []
        #n = len(changed)
        #for i in range(n):
        #    a = changed[i] // 2
        #    try: 
        #        changed.index(a)
        #        if changed.index(a) == 1:
        #            continue
        #        else: 
        #            res.append(a)
        #    except:
        #        continue
        #return set(res) 