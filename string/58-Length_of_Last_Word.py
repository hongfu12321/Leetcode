class Solution:
    def lengthOfLastWord(self, s: str) -> int:
#         i, count = len(s) - 1, 0    
#         while i >= 0 and s[i] == ' ':
#             i -= 1       
#         while i >= 0 and s[i] != ' ':
#             count += 1
#             i -= 1        
#         return count

        words = s.split()
        return len(words[-1]) if words else 0
