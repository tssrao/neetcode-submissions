class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = [i for i in s]
        chars_t = [i for i in t]
        print(chars_s)
        if len(s) == len(t) and sorted(chars_s) == sorted(chars_t):
            return True
        else:
            return False 
        