class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                # 자료형을 초과하지 않는 중앙 위치 계산
                mid = left + (right - left) // 2
                
                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1
            
        return binary_search(0, len(nums) - 1)