class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for str in strs:
            key = "".join(sorted(str))
            if key not in d:
                d[key] = [str]
            else:
                d[key].append(str)
        return d.values()