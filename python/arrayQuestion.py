import bisect
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row = len(grid)
    ret = 0
    repeat = 0
    if row ==0:
        return ret
    col = len(grid[0])
    if col ==0:
        return ret
    for i in range(0,row):
        for j in range(0,col):
            if grid[i][j] ==1:
                ret+=1
                if i!=0 and grid[i-1][j] ==1:
                    repeat+=1
                if j!=0 and grid[i][j-1] ==1:
                    repeat+=1
    return 4*ret-repeat*2

def testList(l):
    print len(l)
    l.pop()
    print len(l)

def findTargetSumWays(nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    "too conflict and has chongfu "
    if len(nums)==0:
        if S ==0:
            return 1
        else:
            return 0
    tmp = nums.pop()
    l = findTargetSumWays(nums,S-tmp)
    nums.append(tmp)
    tmp = nums.pop()
    r =findTargetSumWays(nums,S+tmp)
    nums.append(tmp)
    return l+r

def wiggleMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)<2:
        return len(nums)
    stack = [nums[0]]
    neg =None 
    for i in range(1,len(nums)):
        n = nums[i]
        import pdb
        pdb.set_trace()
        if n>stack[-1]:
            if neg ==None or neg ==False:
                stack.append(n)
                neg =True
            else:
                stack.pop()
                stack.append(n)
        else:
            if neg==None or neg == True:
                stack.append(n)
                neg = False
            else:
                stack.pop()
                stack.append(n)
    return len(stack)

def binarySearch(nums,target):
    l = 0
    r = len(nums)
    while l<r:
        mid = (l+r)/2
        if nums[mid]<=target:
            l = mid+1
        else:
            r = mid
    return l-1

def findRightInterval(intervals):
    l = sorted((e.start, i) for i, e in enumerate(intervals))
    res = []
    for e in intervals:
        r = bisect.bisect_left(l, (e.end,))
        res.append(l[r][1] if r < len(l) else -1)
    return res

if __name__ == '__main__':
    # nums = [1,1,1,1,1]
    # tmp = findTargetSumWays(nums,3)
    # print tmp
    # nums = [1,7,4,9,2,5]
    # tmp = wiggleMaxLength(nums)
    # print nums
    # a = Interval(1,4)
    # b = Interval(2,3)
    # c = Interval(5,6)
    # intervals = [a,b,c]
    # tmp = findRightInterval(intervals)
    # print tmp
    # a = [1,2,2,2,2,4]
    # # a.insert(3,10)
    # # tmp = binarySearch(a,2)
    # tmp = str(a)
    # print tmp
    # print 10|1

    b = '1234567'
    print b[0:3]