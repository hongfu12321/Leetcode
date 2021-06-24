class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # edge case: if len(strs) <= 1 -> return [strs]
        # Create a dictionay, store the tuple of sorted string as key, and the index as value
        # If key is in the dictionary, append string into the result array at value
        # If it's not in the dictionary, append a new array in result and update the index
        
    
        if len(strs) <= 1: return [strs]
        
        dic = collections.defaultdict(list)
        for s in strs:
            dic[tuple(sorted(s))].append(s)
        
        return dic.values()
    
    
# Runtime: 84 ms, faster than 99.01% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.9 MB, less than 44.71% of Python3 online submissions for Group Anagrams.
'''
Time complexity:
    N is length of strs. K is length of every string. Sort string is Klong(K).
    Total = O(NKlogK).
Space complexity:
    dic size = N * K
    Total = O(NK)
'''
