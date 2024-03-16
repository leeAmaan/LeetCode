class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt = 0 
        max_len = 0
        cnt_map = {0:-1}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt -= 1
            else:
                cnt += 1
            
            if cnt in cnt_map:
                max_len = max(max_len, i - cnt_map[cnt])
            else:
                cnt_map[cnt] =i
        return max_len
        
        
        # print(Counter(nums))