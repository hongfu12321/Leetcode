'''
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
Return the maximum possible length of s.


Example 1:
    Input: arr = ["un","iq","ue"]
    Output: 4
    Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
    Maximum length is 4.

Example 2:
    Input: arr = ["cha","r","act","ers"]
    Output: 6
    Explanation: Possible solutions are "chaers" and "acters".

Example 3:
    Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output: 26
'''

class Solution:
    def maxLength(self, arr) -> int:
        maxLen = 0
        arrLen = len(arr)

        def backtrace(s, idx):
            if idx == arrLen: return
            nonlocal maxLen
            if len(s + arr[idx]) == len(set(s + arr[idx])):
                maxLen = max(maxLen, len(s + arr[idx]))
                
                for i in range(idx, arrLen):
                    backtrace(s + arr[i], i + 1)
        
        backtrace("", 0)
        return maxLen


if __name__ == '__main__':
    stacks = [
        ["un","iq","ue"],
        ["cha","r","act","ers"],
        ["abcdefghijklmnopqrstuvwxyz"],
        ["abcdefghijklm","bcdefghijklmn","cdefghijklmno","defghijklmnop","efghijklmnopq","fghijklmnopqr","ghijklmnopqrs","hijklmnopqrst","ijklmnopqrstu","jklmnopqrstuv","klmnopqrstuvw","lmnopqrstuvwx","mnopqrstuvwxy","nopqrstuvwxyz","opqrstuvwxyza","pqrstuvwxyzab"]
    ]

    answers = [
        4, 
        6, 
        26,
        26,
    ]
    
    func = Solution()
    for stack, answer in zip(stacks, answers):
        res = func.maxLength(stack)
        print("{} - [{}, {}]".format(res == answer, res, answer))