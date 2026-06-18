class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        output = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        list_1 = [[] for _ in range(len(nums) + 1)]
        for key, value in counts.items():
            list_1[value].append(key)
        for item in reversed(list_1):
            if k == 0: break
            if item:
                if len(item) > k:
                    output.extend(item[:k])
                    break
                output.extend(item)
                k -= len(item)
        return output