'''
Count minimum swap to make string palindrome
Difficulty Level : Medium

Given a string s, the task is to find out the minimum no of adjacent swaps required to make string s palindrome. If it is not possible, then return -1.

Examples:
Input: aabcb 
Output: 3 
Explanation: 
After 1st swap: abacb 
After 2nd swap: abcab 
After 3rd swap: abcba

Input: adbcdbad 
Output: -1 
'''

import collections

def countSwap(s):
    s, n, count = list(s), len(s), 0

    # count amount of every character, if there are more then one odd amount, return False
    def check_shuffle_palindrome(s):
        check = list(collections.Counter(s).values())
        check = [i for i in check if i % 2]
        return len(check) <= 1

    if not check_shuffle_palindrome(s):
        return -1 

    i = 0
    while i < n // 2:
        left = i
        right = n - left - 1

        # find the same char from right to left
        while left < right:
            if s[left] == s[right]:
                break
            right -= 1

        # If left == right means this char is the single character
        # So we want it swap to the middle
        if left == right:
            s[i], s[i + 1] = s[i + 1], s[i]
            count += 1
            continue

        # Swap the char from right pointer to the mirror position of left
        for j in range(right, n - left - 1):
            s[j], s[j + 1] = s[j + 1], s[j]
            count += 1

        i += 1

    return count            



if __name__ == '__main__':
    stacks = [
        "aabcb",   # 3
        "mamad",   # 3
        "asflkj",  # -1
        "aabb",    # 2
        "ntiin",   # 1
        "acccbba", # 3
    ]

    for s in stacks:
        print(countSwap(s))
