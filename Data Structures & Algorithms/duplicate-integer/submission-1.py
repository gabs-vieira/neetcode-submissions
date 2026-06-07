class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {
            n: 0
            for n in nums
        }
         
        for n in nums:
            num_map[n]+=1
            if num_map[n] > 1:
                return True

        return False
