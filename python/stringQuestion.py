def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if len(num1) < len(num2):
        return addStrings(num2,num1)
    ret = ""
    i = len(num1)-1
    j = len(num2)-1
    pre =0
    print num1
    print num2
    while i>=0 and j>=0:
        num = int(num1[i])+int(num2[j]) + pre
        tmp = (num)%10
        ret = str(tmp)+ret
        pre = num/10
        i-=1
        j-=1
    while i>=0:
        num = int(num1[i]) + pre
        tmp = num%10
        pre = num/10
        ret =str(tmp)+ret
        i-=1
    if pre==1:
        ret ="1"+ret
    return ret

if __name__ == '__main__':
    num1 = "9"
    num2 ="99"
    print addStrings(num1,num2)