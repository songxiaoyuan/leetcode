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

if __name__ == '__main__':
    s = '10'
    tmp = numDecodings(s)
    print tmp
    a = 'abc'
    b = a[:]
    print a==b