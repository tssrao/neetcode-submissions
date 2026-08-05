class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # # O(n**2) time complexity
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):

        #         if nums[i] + nums[j] == target:
        #             res.append(i)
        #             res.append(j)
        #             return res


        # One pass hash - O(n)

        dict_map = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in dict_map:
                res.append(dict_map[target - nums[i]])
                res.append(i)
                return res
            else:
                dict_map[nums[i]] = i 
        