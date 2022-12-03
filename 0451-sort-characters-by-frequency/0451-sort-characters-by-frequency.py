class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the occurence on each character
        cnt = collections.defaultdict(int)
        for c in s:
            cnt[c] += 1

        # Sort and Build string
        res = []
        for k, v in sorted(cnt.items(), key = lambda x: -x[1]):
            res += [k] * v
        return "".join(res)