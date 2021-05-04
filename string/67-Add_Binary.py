class Solution:
    def addBinary(self, a: str, b: str) -> str:
        list_a = list(a)
        list_b = list(b)
        
        res = ""
        carry = 0
        while list_a or list_b or carry:
            if list_a:
                carry += int(list_a.pop())
            if list_b:
                carry += int(list_b.pop())
            
            carry, bit = divmod(carry, 2)
            res += str(bit)
            
        return res[::-1]
    
'''
Runtime: 28 ms, faster than 89.54% of Python3 online submissions for Add Binary.
Memory Usage: 14.2 MB, less than 80.90% of Python3 online submissions for Add Binary.
'''