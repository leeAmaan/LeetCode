class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people: 
            return []

        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, result = {}, [], []
        
        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()      # here are different heights we have

        # sort from the tallest group
        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                result.insert(p[0], people[p[1]])

        return result