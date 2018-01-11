def getNext(s):
    ret =[0]*(len(s)+1)
    j = 0
    for x in xrange(1,len(s)):
        while j>0 and s[j] != s[x]:
            j = ret[j]
        if s[j] == s[x]:
            j+=1
        ret[x+1] = j
    return ret

def findLength(target,find,next):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    j = 0
    for x in xrange(0,len(target)):
        while j>0 and target[x] != find[j]:
            j = next[j]
        if target[x] == find[j]:
            j+=1
        if j == len(find):
            return x-j+1
    return -1


if __name__ == '__main__':
    s = "abcdabcdf"
    f = "abcde"
    tmp =getNext(s)
    print tmp
    ret = findLength(s,f,tmp)
    print ret





