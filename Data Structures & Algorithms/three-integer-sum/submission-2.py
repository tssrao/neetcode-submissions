class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort + 2 pointer

        nums = sorted(nums)
        # print(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left_ptr = i+1
            right_ptr = (len(nums))-1

            # print(i)
            
            while left_ptr < right_ptr:
                # i + x + y = 0 -> add triplet

                total = nums[i] + nums[left_ptr] + nums[right_ptr]

                if total == 0:
                    res.append([nums[i], nums[left_ptr], nums[right_ptr]])
                    left_ptr += 1
                    right_ptr -= 1

                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr - 1]:
                        left_ptr += 1

                    while left_ptr < right_ptr and nums[right_ptr] == nums[right_ptr + 1]:
                        right_ptr -= 1
                    # print(res)

                elif total < 0:
                    left_ptr += 1

                else:
                    right_ptr -= 1


        return res