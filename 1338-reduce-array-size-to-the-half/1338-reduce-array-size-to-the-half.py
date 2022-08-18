class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_len = len(arr)
        target_len = total_len // 2
        count_set = 0
        arr_chr_count = Counter(arr).most_common()
        for x in arr_chr_count:
            total_len -= x[1]
            print(x[1])
            count_set += 1
            print(count_set)
            if total_len <= target_len:
                break
                
        
        return count_set
        
        
        
        
        
        
        
        
        #sa = set(arr)
        #if len(sa)/2 == 0:
        #    return 1 
        #else:
        #    return int(len(sa)/2)
