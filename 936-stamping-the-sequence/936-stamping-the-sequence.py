class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m, target, stamp, res = len(target), len(stamp), list(target), list(stamp), []
        
        def check(i):
            changed = False
            for j in range(m):
                if target[i + j] == '?': continue
                if target[i + j] != stamp[j]: return False
                changed = True 
            if changed:
                target[i:i + m] = ['?'] * m
                res.append(i)
            return changed
        
        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= check(i)
        return res[::-1] if target ==['?'] * n else []