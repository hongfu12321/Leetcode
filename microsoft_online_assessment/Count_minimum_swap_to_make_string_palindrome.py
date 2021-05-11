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

        while left < right:
            if s[left] == s[right]:
                break
            right -= 1

        if left == right:
            s[i], s[i + 1] = s[i + 1], s[i]
            count += 1
            continue

        for j in range(right, n - left - 1):
            s[j], s[j + 1] = s[j + 1], s[j]
            count += 1

        i += 1

    return count            



if __name__ == '__main__':
    print(countSwap("aabcb"))   # 3
    print(countSwap("mamad"))   # 3
    print(countSwap("asflkj"))  # -1
    print(countSwap("aabb"))    # 2
    print(countSwap("ntiin"))   # 1
    print(countSwap("acccbba")) # 3
