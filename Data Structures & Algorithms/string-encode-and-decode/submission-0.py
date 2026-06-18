class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            num = s[i:j]
            range_slicing = int(num)
            start_slicing = j + 1
            end_slicing = start_slicing + range_slicing
            output.append(s[start_slicing:end_slicing])
            i = end_slicing
        return output