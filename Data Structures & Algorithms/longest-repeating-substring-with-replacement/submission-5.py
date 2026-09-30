# class Solution:

#     def get_max_frequency(self, s):
#         res = {}
#         for i in s:
#             if i in res:
#                 res[i] += 1
#             else:
#                 res[i] = 1
#         l = []
#         for i, j in res.items():
#             l.append(j)
#         return max(l)

#     def characterReplacement(self, s: str, k: int) -> int:

#         start_pos = 0
#         end_pos = 0
#         repetitions_req = 0
#         max_len = 0


#         while start_pos <= end_pos & end_pos <= len(s):
#             curr_sub_str = s[start_pos:end_pos+1]
#             max_freq = self.get_max_frequency(curr_sub_str)
#             win_len = len(curr_sub_str)

#             rep_needed = win_len - max_freq


#             if rep_needed <= k:
#                 end_pos += 1
#             else:
#                 start_pos += 1
#             max_len = max(len(s[start_pos: end_pos]), max_len)

#             # print(f'win: {curr_sub_str}, max_freq: {max_freq}, rep_needed: {rep_needed}, max_len: {max_len}, s:{start_pos}, e:{end_pos}')
#         return max_len
        

 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start_pos = 0
        end_pos = 0
        repetitions_req = 0
        max_len = 0
        res = {}

        while start_pos <= end_pos and end_pos < len(s):
            curr_sub_str = s[start_pos:end_pos+1]

            if len(curr_sub_str) > sum(res.values()):
                curr_char = s[end_pos]
                res[curr_char] = res.get(curr_char, 0) + 1

            max_freq = max(res.values())
            win_len = len(curr_sub_str)
            rep_needed = win_len - max_freq

            if rep_needed <= k:
                max_len = max(win_len, max_len)
                end_pos += 1
            else:
                res[s[start_pos]] -= 1
                start_pos += 1

        return max_len       