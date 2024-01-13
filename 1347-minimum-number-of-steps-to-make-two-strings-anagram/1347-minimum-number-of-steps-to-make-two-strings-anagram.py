class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = [0] * 26
        count_t = [0] * 26
        
        for char in s:
            count_s[ord(char) - ord('a')] += 1
        
        for char in t:
            count_t[ord(char) - ord('a')] += 1
        
        steps = 0
        for i in range(26):
            steps += abs(count_s[i] - count_t[i])
        
        return steps //2
            
        
        
        
        
#         list_s = sorted(list(s))
#         list_t = sorted(list(t))
#         # print(list_s)
#         # print(list_t)
#         res = 0
#         for i in range(len(list_s)):
#             if list_s[i] in list_t:
#                 list_t.remove(list_s[i])
#                 res += 1
        
#         return len(list_s) - res