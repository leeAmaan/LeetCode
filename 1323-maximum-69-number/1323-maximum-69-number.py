def convert(list):
        s = [str(i) for i in list]
        res = int("".join(s))
        return res 


class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = [int(x) for x in str(num)]
        for i in range(len(ans)):
            if ans[i] == 6:
                ans[i] = 9
                return convert(ans) 
        return convert(ans)
    
    
    
        
        
       # for i in range(len(num)):
        #    a = b
         #   a = num / 10 ** (len(num)- i)
          #  b = num % 10 ** (len(num)- i)
           #if a == 6:
            #   r    urn b +  
            
            