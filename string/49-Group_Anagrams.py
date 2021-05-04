class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: return [strs]
        
        dic = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in dic:
                dic[sort_s].append(s)
            else:
                dic[sort_s] = [s]

        return dic.values()
    

'''
Runtime: 80 ms, faster than 99.76% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.7 MB, less than 62.31% of Python3 online submissions for Group Anagrams.
'''
