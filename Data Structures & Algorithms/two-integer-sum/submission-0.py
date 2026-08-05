class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tot = 0
        for i in range(len(nums)):
            for j in range(i):
                tot = nums[i] + nums[j]
                if tot == target:
                    return [j, i]
        