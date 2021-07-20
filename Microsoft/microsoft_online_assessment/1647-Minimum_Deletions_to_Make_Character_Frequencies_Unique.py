'''
1647. Minimum Deletions to Make Character Frequencies Unique
Medium

A string s is called good if there are no two different characters in s that have the same frequency.
Given a string s, return the minimum number of characters you need to delete to make s good.
The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

example1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

example2:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

'''

import collections

class Solution:
    def minDeletions(self, s: str) -> int:
        # count every character amount in the sting, and return the value only.
        s_lst = list(collections.Counter(s).values())

        freq, count = set(), 0
        for i in s_lst:
            while i in freq:
                i -= 1
                count += 1
            if i > 0:
                freq.add(i)

        return count
        


if __name__ == '__main__':
    ans = Solution()
    print(ans.minDeletions(""))
    print(ans.minDeletions("aab"))
    print(ans.minDeletions("ceabaacb"))
    print(ans.minDeletions("abcdef"))

