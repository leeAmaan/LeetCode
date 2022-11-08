class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        for i in s:
            if not res:
                res.append(i)
            elif res[-1].isupper() and res[-1].lower() == i:
                res.pop()
            elif res[-1].islower() and res[-1].upper() == i:
                res.pop()
            else:
                res.append(i)

        return ''.join(res) 
    
    
     #a = list(s)
     #   for i in range(len(a)):
     #       if a[i] == a[i+1]:
     #           del a[i:i+1]
     #   res = a