class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Time Complexity = O(n * klogk); sorting: k log k
        seen_dict = {}
        final_res = []

        for i in strs:
            # print(i)
            current_sorted_str = sorted(i)
            joined_str = ''.join(current_sorted_str)
            # print(joined_str)

            # print(seen_dict)
            if joined_str in seen_dict:
                seen_dict[joined_str].append(i)

            else:

                seen_dict[joined_str] = [i]
        
        # print(seen_dict)

        for i in seen_dict:
            final_res.append(seen_dict[i])
        return final_res