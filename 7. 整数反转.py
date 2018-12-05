'''
给定一个32位有符号整数，将整数中的数字进行反转。
示例1：输入：123输出：321示例2：
输入：-123输出：-321示例3：输入：120输出：21注意：
假设我们的环境只能存倩32.位有符号整数，其数值范围是[-2^31，2^31-1.根据这个假设，如果反转后的整数产出，则返回0。
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = -int(str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])
        return x if -2**31 <= x <= 2**31-1 else 0

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x>=0 else -1
        x_abs = abs(x)
        result = sign * int(str(x_abs)[::-1])
        return result if -2**31 <= result <= 2**31-1 else 0

ss = Solution()
x = 2**30
print(ss.reverse(x))
