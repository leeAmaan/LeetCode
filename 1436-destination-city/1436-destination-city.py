class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return reduce(lambda x, y: y - x, map(set, zip(*paths))).pop()