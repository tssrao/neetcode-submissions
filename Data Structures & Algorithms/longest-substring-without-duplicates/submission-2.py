class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        elif len(s)==1:
            return 1
        left = 0
        right = 1
        max_len = 0
        curr_sub_str = set()
        curr_sub_str.add(s[left])

        while right < len(s):
            if s[right] not in curr_sub_str:
                curr_sub_str.add(s[right])
                right +=1
            else:
                curr_sub_str.remove(s[left])
                left += 1
            max_len = max(max_len, len(curr_sub_str))
        return max_len