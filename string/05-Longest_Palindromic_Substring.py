'''
G-05-Longest Palindromic Substring

Medium

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

Example 2:

    Input: "cbbd"
    Output: "bb"
'''


class Solution:
    def longestPalindrome_classic(self, s: str) -> str:
        startIdx = -1
        maxLen = -1
        strLen = len(s)

        if not s: return s
        for idx in range(strLen):
            def expandFromMiddle(left, right):
                i = 1            
                while left >= 0 and right < strLen and s[left] == s[right]:
                    left -= 1
                    right += 1  
                return right - left - 1

            len1 = expandFromMiddle(idx, idx)
            len2 = expandFromMiddle(idx, idx + 1)

            if len1 > maxLen or len2 > maxLen:
                maxLen = max(len1, len2)
                startIdx = idx - (maxLen - 1) // 2

        return s[startIdx : startIdx + maxLen]


    def longestPalindrome_fast(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]: return s
        start, maxl = -1,0
        
        for i in range(len(s)):
            odd = s[i-maxl-1:i+1]
            even = s[i-maxl:i+1]
            if i - maxl - 1 >= 0 and odd == odd[::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and even == even[::-1]:
                start = i - maxl
                maxl += 1
                
        return s[start:start+maxl]


if __name__ == '__main__':
    stacks = [
        "babad",
        "cbbd"
    ]

    answers = [
        "bab",
        "bb"
    ]
    
    func = Solution()
    for stack, answer in zip(stacks, answers):
        res1 = func.longestPalindrome_classic(stack)
        res2 = func.longestPalindrome_fast(stack)
        print("classic: {} - [{}, {}]".format(res1 == answer, res, answer))
        print("classic: {} - [{}, {}]".format(res2 == answer, res, answer))