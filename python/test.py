# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def testDic(dic):
	dic['a'] = 10

print "this is used to test"
print "fighting"
a = dict()
print a
testDic(a)
print a
print a.get('b',0)
for i in range(5,0,-1):
	print i
aa = [4,3,5,2,6,7]
aa = aa[0:10]
print aa
end = float('-inf')
print end
print 6 >> 1