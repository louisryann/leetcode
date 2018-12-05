'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif str(x) == str(x)[::-1]:
            return True
        else:
            return False

ss = Solution()
x = 121
print(ss.isPalindrome(x))
