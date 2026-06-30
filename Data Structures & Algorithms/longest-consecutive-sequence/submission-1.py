class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqMaxLength = 0
        num1 = set(nums)
        l = len(num1)
        for num in num1:
            if num-1 not in num1:
                currentLength = 1
                while num+1 in num1:
                    num += 1
                    currentLength += 1
                if currentLength > seqMaxLength: seqMaxLength = currentLength
            if seqMaxLength > l/2: return seqMaxLength
        return seqMaxLength
            

            