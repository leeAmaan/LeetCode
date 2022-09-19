class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        par = collections.defaultdict(list)
        for line in paths:
            data = line.split()
            root = data[0]
            for file in data[1:]:
                name, _, content = file.partition('(')
                par[content[:-1]].append(root + '/' + name)
                
        return [x for x in par.values() if len(x) > 1]