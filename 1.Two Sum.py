
#题目：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。

#你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

'''
这道题给了我们一个数组，还有一个目标数target，让我们找到两个数字，使其和为target，
 乍一看就感觉可以用暴力搜索，但是猜到OJ肯定不会允许用暴力搜索这么简单的方法，
 于是去试了一下，果然是Time Limit Exceeded，这个算法的时间复杂度是O(n^2)。
 那么只能想个O(n)的算法来实现，由于暴力搜索的方法是遍历所有的两个数字的组合，
 然后算其和，这样虽然节省了空间，但是时间复杂度高。一般来说，我们为了提高时间的复杂度，
 需要用空间来换，这算是一个trade off吧，我们只想用线性的时间复杂度来解决问题，
 那么就是说只能遍历一个数字，那么另一个数字呢，我们可以事先将其存储起来，使用一个HashMap，
 来建立数字和其坐标位置之间的映射，我们都知道HashMap是常数级的查找效率，
 这样，我们在遍历数组的时候，用target减去遍历到的数字，就是另一个需要的数字了，
 直接在HashMap中查找其是否存在即可，注意要判断查找到的数字不是第一个数字，
 比如target是4，遍历到了一个2，那么另外一个2不能是之前那个2，
 整个实现步骤为：先遍历一遍数组，建立HashMap映射，然后再遍历一遍，开始查找，找到则记录index。代码如下：
'''

'''步骤：
1.建立字典 lookup 存放第一个数字，并存放该数字的 index
2.判断 lookup 种是否存在： target - 当前数字， 则表面 当前值和 lookup中的值加和为 target.
3.如果存在，则返回： target - 当前数字 的 index 和 当前值的 index

'''

class Solution(object):

    def twoNum(self,nums,target):
        lookup = {}
        for i,num in enumerate(nums):
            if target-num in lookup:     #和为两个数，num其实为第二个数，判断的是第一个数字在不在
                return [lookup[target-num],i]
            else:
                lookup[num] = i          #建立字典 lookup 存放第一个数字，并存放该数字的 index

nums = [2, 7, 11, 15]
target = 9
ss = Solution()
print(ss.twoNum(nums,target))