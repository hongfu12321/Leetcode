class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        res = "1"
        
        for _ in range(1, n):
            count = 1
            pre = res[0]
            tmp = ""
            i = 1
            while i < len(res):
                if res[i] != pre:
                    tmp = tmp + str(count) + pre
                    pre = res[i]
                    count = 1
                else:
                    count += 1
                i += 1
                    
            res = tmp + str(count) + pre

            
        return res
    
'''
Runtime: 40 ms, faster than 85.63% of Python3 online submissions for Count and Say.
Memory Usage: 14.5 MB, less than 24.46% of Python3 online submissions for Count and Say.
'''