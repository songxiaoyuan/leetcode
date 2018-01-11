# -*- coding:utf-8 -*-
def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    if k>=len(arr):
        return arr
    l = 0
    r = len(arr)-1
    m_k = r
    while l<r:
        mid = l + (r-l)/2
        print mid
        if mid+k > len(arr)-1:
        	m_k = len(arr)-1
        else:
        	m_k = mid + k
        if (x - arr[mid]) > (arr[m_k]-x):
            l = mid+1
        else:
            r = mid
    if (l + k)>len(arr):
    	return arr[len(arr)-k:len(arr)]
    return arr[l:l+k]



if __name__ == '__main__':
	arr = [0,0,1,2,3,3,4,7,7,8]
	k =3
	x =5
	tmp = findClosestElements(arr,k,x)
	print tmp
	# a = [1,2,3,4,5]
	# print a[2:5]