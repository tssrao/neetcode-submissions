class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. Use a dictionary (hash map) to store counts
        dup_dict = {}
        res = False
        
        for i in nums:
            # 2. Check if the number is already a key in our dictionary
            if i in dup_dict:
                dup_dict[i] += 1
            else:
                # 3. If it's the first time seeing it, initialize to 1
                dup_dict[i] = 1
            
            # 4. If any count goes above 1, we found a duplicate
            if dup_dict[i] > 1:
                res = True
                break  # Optimization: stop looking once we find one
                
        return res