class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def largestValues(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    ret = []
    que = [root,None]
    tmp = None
    while len(que)!=0:
        node = que.pop(0)
        if node==None:
            ret.append(tmp)
            tmp=None
            if len(que)==0:
                return ret
            else:
                que.append(None)
        else:
            tmp = max(tmp,node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
    return ret

def findFrequentTreeSum(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root ==None:
        return []
    dic = dict()
    help(root,dic)
    print dic
    num = max(dic.items(),key = lambda x:x[1])[1]
    ret = []
    print num
    for item in dic:
        if dic[item] ==num:
            ret.append(item)
    return ret
    
def help(root,dic):
    if root==None:
        return 0
    s = help(root.left,dic)+help(root.right,dic)+root.val
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] +=1
    return s

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(-3)
    tmp = findFrequentTreeSum(root)
    print tmp