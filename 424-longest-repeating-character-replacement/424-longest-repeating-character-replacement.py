class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = result = 0
        counts = collections.Counter()
        for i in range(len(s)):
            counts[s[i]] += 1
            maxf = max(maxf, counts[s[i]])
            if result - maxf < k:
                result += 1
            else:
                counts[s[i - result]] -= 1
        return result
            