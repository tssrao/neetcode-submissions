class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_map = {}

        for i in nums:
            if i in dict_map:
                dict_map[i] += 1
            else:
                dict_map[i] = 1
            
            if dict_map[i] > 1:
                return True

        return False         