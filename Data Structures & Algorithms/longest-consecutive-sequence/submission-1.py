class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        
        seq_start = []
        max_len = 0

        for i in nums:
            # find start of sequence; if num - 1 is not present, then it is start of a sequence
            if i-1 not in nums:
                seq_start.append(i)
                # print(seq_start)
                len = 1
                # print(i)

                # for every start of seq, loop and see till how long i+1 is available in the input
                while i + len in nums:
                    # print('     ',1+len)
                    len += 1
                if len > max_len:
                    max_len = len
                # print('')
        
        return max_len