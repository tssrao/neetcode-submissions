class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        sorted_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        ans = []

        for num, count in sorted_items[:k]:
            ans.append(num)

        return ans
        