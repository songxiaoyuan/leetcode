def order(array,index,n,ret):
	# import pdb
	# pdb.set_trace()
	if n==index:
		ret.append(array[:])
		return
	# order(array,index+1,n,ret)
	for i in range(index,n):
		array[i],array[index] = array[index],array[i]
		order(array,index+1,n,ret)
		array[i],array[index] = array[index],array[i]

def help(array,index,N,ret):
	if index==N:
		ret.append(array[:])
		return 1
	# import pdb
	# pdb.set_trace()
	num = 0
	for i in range(index,N):
		array[i],array[index] = array[index],array[i]
		# if array[0]==4 and array[1] == 6 and array[2] == 1 and array[3] == 2 and array[4] == 5 and array[5] == 3:
		# 	import pdb
		# 	pdb.set_trace
		if (array[index]%(index+1)==0 or (index+1)%array[index]==0):
			num +=help(array,index+1,N,ret)
		array[i],array[index] = array[index],array[i]
	return num

def countArrangement(N):
	"""
	:type N: int
	:rtype: int
	"""
	ret = []
	counter = 0
	queue = []
	x = []
	queue.append(x);
	while(len(queue) >0):
		x = queue.pop()
		if len(x) == N:
			ret.append(x)
			counter+=1
		else:
			for i in range(1,N+1):
				y = x[:]
				if i not in y:
					if (i % (len(y)+1) ==0) or ((1+len(y)) % i ==0):
						y.append(i)
						queue.append(y)
	return ret

if __name__ == '__main__':
	array = [1,2,3]
	# array[0],array[1] = array[1],array[0]
	# print array
	ret =[]
	order(array,0,3,ret)
	for item in ret:
		print item
	# tmp = help(array,0,2)
	# print tmp
	# tmp = countArrangement(6)
	# # for item in tmp:
	# # 	print item
	# # print '*'*20
	# ret =[]
	# help(array,0,6,ret)
	# print len(ret)
	# for item in ret:
	# 	print item
	print 1^3
