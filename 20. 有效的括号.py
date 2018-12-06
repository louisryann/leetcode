class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        return True if s =='' else False

#解法二 栈