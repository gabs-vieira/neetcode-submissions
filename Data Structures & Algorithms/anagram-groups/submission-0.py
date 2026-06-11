class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        group = {}
        for st in strs:
            key = "".join(sorted(st))

            if key not in group:
                group[key] = []

            group[key].append(st)
            
        return list(group.values())
