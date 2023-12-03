class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = nums1 + nums2
        mid.sort()
        i = len(mid)
        if len(mid)%2 ==0 :
            ans = (mid[i//2] + mid[(i//2-1)])/2   
        else:
            ans = mid[i//2]  
        return ans
        
        