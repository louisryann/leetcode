'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

'''


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
#解法1
        #return  haystack.find(needle)   #re模块中findall,match,search

#解法2
        len1 = len(haystack)
        len2 = len(needle)
        for i in range(len1-len2+1):
            if haystack[i:i+len2] == needle:
                return i
        return -1

