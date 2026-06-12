from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        sorted_items = sorted(
            counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [num for num, freq in sorted_items[:k]]