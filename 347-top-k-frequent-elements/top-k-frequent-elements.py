import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use Counter to get frequencies in O(n) time
        counts = Counter(nums)

        # Use a min-heap of size k to track the top k frequent elements
        # We store tuples of (frequency, element) in the heap
        min_heap = []
        for num, count in counts.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Extract the elements from the heap
        return [num for count, num in min_heap]