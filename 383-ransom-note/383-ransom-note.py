class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print(collections.Counter(ransomNote) - collections.Counter(magazine))
        return not collections.Counter(ransomNote) - collections.Counter(magazine)