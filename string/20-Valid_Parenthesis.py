'''
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        
        for c in s:
            if c not in match:
                stack.append(c)
            else:
                if not stack or match[c] != stack.pop():
                    return False
        return len(stack) == 0
        