# a = [1, 2, 3, 4, 5, 6]
# print(id(a)) # 4536684360
# def test(a):
#     print("a in test - ", id(a)) # a in test - 4536684360
#     a[0] = 1
#     print("a2 in test - ", id(a)) # a2 in test - 4536684360
#     a[0] = 2
#     print("a3 in test - ", id(a)) # a3 in test - 4536684360
#     print("a4 in test - ", id(a[2:])) # a4 in test - 4536684424
#     print("a5 in test - ", id(a[:2])) # a4 in test - 4536684424
#     print("a6 in test - ", id(a[::-1])) # a4 in test - 4536684424
#     b = a[2:]
#     print("b1 in test - ", id(b)) # b1 in test -  4515692424
# test(a)
# print("out1 - ", id(a)) # out1 -  4536684360
# print("-------------------")

# a = [1, 2, 3, 4, 5, 6]
# stack = []
# def test2(a, level):
#     if not a: return
#     mid = len(a) // 2
#     print(level, a, id(a))
#     stack.append([level, a, id(a)])
#     if len(a) > 1:
#         test2(a[:mid], level + 1)
#         test2(a[mid:], level + 1)
# test2(a, 0)

# print("-----------------")
# stack = sorted(stack)
# for i in stack:
#     print(i)

'''
0 [1, 2, 3, 4, 5, 6] 4393918344
1 [1, 2, 3] 4394865352
2 [1] 4394510088
2 [2, 3] 4394865608
3 [2] 4394867592
3 [3] 4394867656
1 [4, 5, 6] 4394867912
2 [4] 4394868040
2 [5, 6] 4394868168
3 [5] 4394867720
3 [6] 4394868360
-----------------
[0, [1, 2, 3, 4, 5, 6], 4393918344]
[1, [1, 2, 3], 4394865352]
[1, [4, 5, 6], 4394867912]
[2, [1], 4394510088]
[2, [2, 3], 4394865608]
[2, [4], 4394868040]
[2, [5, 6], 4394868168]
[3, [2], 4394867592]
[3, [3], 4394867656]
[3, [5], 4394867720]
[3, [6], 4394868360]
'''



class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        leng = [s1_len, s2_len, s3_len] = list(map(len, [s1, s2, s3]))
        if s3_len != s1_len + s2_len: return False
        
        print("length = ", leng)
        def match(i1, i2, i3):
            res1 = res2 = False
            if i1 == s1_len and i2 == s2_len and i3 == s3_len:
                print("In true")
                return True
            if i1 < s1_len and s3[i3] == s1[i1]:
                print("IN 1: {}|{}, {}|{}".format(i1, s1[i1], i3, s3[i3]))
                res1 = match(i1 + 1, i2, i3 + 1)
            if i2 < s2_len and s3[i3] == s2[i2]:
                print("IN 2: {}|{}, {}|{}".format(i2, s2[i2], i3, s3[i3]))
                res2 = match(i1, i2 + 1, i3 + 1)
            
            # print(res1, res2)
            return res1 or res2  
        return match(0, 0, 0)

[s1, s2, s3] = [
    "aabc",
    "abad",
    "aabcabad"
]
print(Solution().isInterleave(s1, s2, s3))