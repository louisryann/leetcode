'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        begin = 0
        end = 1
        tmp = 1
        for i in range(len(s)):
            if s[end] in s[begin:end]:
                tmp = 1
                begin = end


