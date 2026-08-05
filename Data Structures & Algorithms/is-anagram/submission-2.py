class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # O(n logn) time complexity
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        # O(n) complexity
        dict_map = {}

        for i in s:
            dict_map[i] = dict_map.get(i, 0) + 1

        for j in t:
            if j not in dict_map:
                return False

            dict_map[j] -= 1

            if dict_map[j] < 0:
                return False

        return True