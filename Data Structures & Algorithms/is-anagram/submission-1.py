class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Same characters, each character appearing the same number of times, regardless (sem considerar) of order 

        if (len(s) != len(t)):
            return False

        lib = {}
        for k in s:
            if k in lib:
                lib[k] += 1
            else:
                lib[k] = 1

        for k in t:
            if k in lib:
                lib[k] -= 1
            
            if k not in lib:
                return False

        
        for i in lib:
            if lib[i] != 0:
                return False

        return True
