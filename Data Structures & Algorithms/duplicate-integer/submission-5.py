class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Using Hashset

        #Time and Space complexity = O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True

            seen.add(num)
        return False