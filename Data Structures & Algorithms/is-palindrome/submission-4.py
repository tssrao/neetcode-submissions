class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        reversed_str = []
        for i in range(len(s)-1,-1,-1):
            if s[i].lower() in valid_chars:
                reversed_str.append(s[i].lower())
        # print(reversed_str)

        actual_str = []
        for i in s:
            if i.lower() in valid_chars:
                actual_str.append(i.lower())
        # print(actual_str)

        if actual_str == reversed_str:
            return True
        else:
            return False
        