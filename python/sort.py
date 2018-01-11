def bubble(nums):
	if len(nums)<2:
		return
	for i in range(0,len(nums)-1):
		for j in range(0,len(nums)-i-1):
			if nums[j]>nums[j+1]:
				nums[j],nums[j+1] = nums[j+1],nums[j]

def quick(nums,low,high):
	if low>=high:
		return
	flag = nums[low]
	l = low
	h = high
	while l<h:
		while l<h and nums[h]>=flag:
			h-=1
		nums[l] = nums[h]
		while l<h and nums[l]<=flag:
			l+=1
		nums[h] = nums[l]
	nums[l] = flag
	quick(nums,low,l-1)
	quick(nums,l+1,high)

def heapfy(nums,i,size):
	m = i
	l = i*2+1
	r = l+1
	if l<size and nums[m]>nums[l]:
		m = l
	if r<size and nums[m]>nums[r]:
		m = r
	if m !=i:
		nums[i],nums[m] = nums[m],nums[i]
		heapfy(nums,m,size)
def heap(nums):
	l = len(nums)
	for i in range(l/2-1,-1,-1):
		heapfy(nums,i,l)
def heapSort(nums):
	heap(nums)
	for i in range(len(nums)-1,-1,-1):
		nums[0],nums[i] = nums[i],nums[0]
		heapfy(nums,0,i)

def findK(nums,l,r,target):
	if l>=r:
		return
	low = l
	high = r
	poivt = nums[l]
	while l<r:
		while l<r and nums[r]>=poivt:
			r-=1
		nums[l] = nums[r]
		while l<r and nums[l]<=poivt:
			l+=1
		nums[r] = nums[l]
	nums[l] = poivt
	if l==target:
		return nums[l]
	elif l>target:
		return findK(nums,low,l-1,target)
	else:
		return findK(nums,l+1,high,target)


def findSingle(nums,left,right):
	import pdb
	# pdb.set_trace()
	if left > right:
		return -1
	if left==right:
		return left

	mid = left + (right - left)/2
	print mid
	if mid==left:
		if nums[left] == nums[left +1]:
			tmp = findSingle(nums,left+2,right)
			return tmp
	if nums[mid] == nums[mid-1]:
		tmp = findSingle(nums,left,mid-2)
		if tmp != -1:
			return tmp
		tmp = findSingle(nums,mid+1,right)
		if tmp != -1:
			return tmp
		return -1
	elif nums[mid] == nums[mid+1]:
		tmp = findSingle(nums,left,mid-1)
		if tmp != -1:
			return tmp
		tmp = findSingle(nums,mid+2,right)
		if tmp != -1:
			return tmp
		return -1
	else:
		return mid

	


def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) ==1:
    	return nums[1]
    left = 0
    right = len(nums) -1
    while left < right:
    	mid = left + (right - left)/2
    	if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
    		return nums[mid]
    	if nums[mid] == nums[mid+1]:
    		if mid %2 ==0:
    			left = mid+2
    		else:
    			right = mid -1
    	else:
    		if mid%2 ==1:
    			left = mid+1
    		else:
    			right = mid-2
    return nums[left]

if __name__ == '__main__':
	nums = [1,1,2,2,4,4,5,5,9]
	tmp = singleNonDuplicate(nums)
	print tmp