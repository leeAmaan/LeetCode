from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_lose = list(zip(*matches))
        # print(win_lose)
        no_lost = set(win_lose[0])
        # print(no_lost)
        
        one_lost = []
        
        count_lost = Counter(win_lose[1])
        
        for key in count_lost.keys():
            if count_lost[key] > 0 and key in no_lost:
                no_lost.remove(key)
            if count_lost[key]==1:
                one_lost.append(key)
        
        return [sorted(list(no_lost)), sorted(list(one_lost))]
        
        # win = []
        # lose = []
        # for i in range(len(matches)):
        #     win.append(matches[i][0])
        #     lose.append(matches[i][1])
        # res = set(win)-set(lose)
        # lose = Counter(lose)        
        # x = {key: value for key, value in lose.items() if value < 2}
        # lose = list(x.keys())
        # return[res, sorted(lose)]