class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # /Complexity: O(n logn) for sorting; Bucket sort to get O(n)
        dic = {}

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        sort_keys = sorted(dic.values(), reverse=True)

        new_dic = {}

        for key, val in dic.items():
            if val in new_dic:
                new_dic[val].append(key)
            else:
                new_dic[val] = [key]

        res = []

        for freq in sort_keys:
            for num in new_dic[freq]:
                if len(res) < k:
                    res.append(num)
                else:
                    return res

            # Prevent duplicates if the same frequency appears again
            new_dic[freq] = []

        return res