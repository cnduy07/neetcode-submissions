class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            counts = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                counts[index] += 1
            tup = tuple(counts)
            result.setdefault(tup, []).append(s)
        return list(result.values())

