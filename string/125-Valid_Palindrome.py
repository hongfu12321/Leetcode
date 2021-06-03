'''
125. Valid Palindrome
Easy

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
#         left, right = 0, len(s) - 1
        
#         s = s.lower()
#         while left < right:
#             while left < len(s) and not s[left].isalnum():
#                 left += 1
#             while right >= 0 and not s[right].isalnum():
#                 right -= 1
            
#             if left >= right:
#                 if right >= 0 and left < len(s) and s[left] != s[right]: return False
#                 return True
                
#             if s[left] != s[right]: return False
            
#             left += 1
#             right -= 1
        
#         return True

        s = s.lower()
    
        string = []
        for c in s:
            if c.isalnum():
                string.append(c)
                
        return string == string[::-1]

        