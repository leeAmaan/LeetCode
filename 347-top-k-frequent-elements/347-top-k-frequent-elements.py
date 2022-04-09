class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count = collections.Counter(nums)
        freq = Count.most_common(k)
        return list(zip(*freq))[0]