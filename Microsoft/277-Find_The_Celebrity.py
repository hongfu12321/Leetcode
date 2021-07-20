# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    
    '''
    celebrity: everyone knows him, he doesn't know anyone
    normal: someone doesn't know him, he might know someone
    
    '''

    def findCelebrity(self, n: int) -> int:
       
        # To pass typing check from vscode
        def knows(a, b):
            pass

        # find the candidate
        cand = 0
        for i in range(n):
            # if cond knows i, cond is not celebrity
            # if cond don't know i, i is not celebrity
            if knows(cand, i):
                cand = i
                
            # cand don't know anyone after him
            # everyone before cand and after cand is not possible to be celebrity
            # we need to make sure: 
            #   1. cand don't know anyone before him
            #   2. everyone before cand knows cand
            #   3. everyone after cand knows can
            
        for i in range(cand):
            if knows(cand, i):
                return -1
            if not knows(i, cand):
                return -1
            
        for i in range(cand + 1, n):
            if not knows(i, cand):
                return -1
        
        return cand
    
'''
Runtime: 1628 ms, faster than 87.80% of Python3 online submissions for Find the Celebrity.
Memory Usage: 14.5 MB, less than 44.99% of Python3 online submissions for Find the Celebrity.
'''