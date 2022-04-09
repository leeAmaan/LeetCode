class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        basket = [[] for _ in range(len(nums)+1)]
        Count = Counter(nums).items()
        for nums, i in Count:
            basket[i].append(nums)
        num_list = list(chain(*basket))
        return num_list[::-1][:k]