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


if __name__ == '__main__':
	nums = [9,3,4,5,1,8,1,1,7,6]
	# bubble(nums)
	# quick(nums,0,len(nums)-1)
	# heapSort(nums)
	# print nums
	# tmp = findK(nums,0,len(nums)-1,9)
	# print tmp
	# print nums
	# print 11&(-11)
	tmp = []
	for i in range(10):
		tmp.append([10-i,i])
	print tmp
	tmp.sort()
	print tmp