def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s)==0:
        return 0
    if s[0]=='0':
        return 0
    n = len(s)
    dp = [0]*(n+1)
    dp[n] =1 
    if s[n-1] !='0':
        dp[n-1] =1
    # import pdb
    # pdb.set_trace()
    for i in range(n-2,-1,-1):
        if s[i] =='0':
            continue
        else:
            num = int(s[i])*10+int(s[i+1])
            if num<=26:
                dp[i] =dp[i+2]+dp[i+1]
            else:
                dp[i] = dp[i+1]
    return dp[0]

def findLength(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    dp = []
    for i in range(len(A)+1):
        dp.append([0]*(len(B)+1))
    for i in xrange(1,len(A)+1):
        for j in xrange(1,len(B)+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
    for row in dp:
        print row

if __name__ == '__main__':
    A = [1,2,3,4,5,6]
    B = A[2:(1+4)]
    print B





