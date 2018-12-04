'''
from光城LeetCode攀登之旅（16）
'''

#题1：反转字符串中的单词

#方法1
def reverseWord(str):
    strlist = str.split()
    a = [strlist[i][::-1] for i in range(len(strlist))]
    return ' '.join(a)

word = 'This is the voa special english health report'
print(reverseWord(word))


#方法2
class Solution(object):
    def reverseWord(self,s):
        return ' '.join(s[::-1].split()[::-1])

word = 'This is the voa special english health report'
ss = Solution()
print(ss.reverseWord(word))


#题2：除自身以外数组的乘积
class Solution(object):

    def productExceptSelf(self,numlist):
        arr = []
        for i in range(len(numlist)):
            a = self.listProduct(numlist[:i])*self.listProduct(numlist[i+1:])
            arr.append(a)
        return arr

    def listProduct(self,numlist):
        product = 1
        if numlist:
            for num in numlist:
                product *= num
        else:
            product =1
        return product

num = [1,2,3,4]
ss = Solution()
print(ss.productExceptSelf(num))
