class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """freqs = collections.Counter(nums)
        freqs_heap = []
        #print(freqs)
        # ㅎ힙에 음수로 삽입 
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        print(freqs_heap)
        topk = list()
        # k번 만큼 추출, 최소 힙(Min Heap) 이므로 가장 작은 음수 순으로 추출 
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
            print(topk)
        return topk
        """
        #print(list(zip(*collections.Counter(nums).most_common(k))))
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
        
        #Count = collections.Counter(nums)
        #freq = Count.most_common(k)
        #return list(zip(*freq))[0]