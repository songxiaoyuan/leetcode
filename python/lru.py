class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.dict = {}
        self.linkedList = linkedList()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            self.linkedList.remove(node)
            self.linkedList.insert(node)
            return node._val
        else:
            return None
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            node = self.dict[key]
            self.linkedList.remove(node)
            self.linkedList.insert(node)
            node._val = value
            self.dict[key] = node
        else:
            node = Node(value)
            self.dict[key] = node
            if self.size < self.capacity:  
                self.linkedList.insert(node)
                self.size +=1
            else:
                self.linkedList.pop()
                self.linkedList.insert(node)

class Node(object):
    """docstring for Node"""
    def __init__(self, val):
        super(Node, self).__init__()
        self._val = val
        self._pre = None
        self._next =None

class linkedList(object):
    """docstring for linkedList"""
    def __init__(self):
        super(linkedList, self).__init__()
        self._head = None
        self._tail = None

    def insert(self,node):
        if self._head ==None:
            self._head = node
            self._tail = node
            node._pre = None
            node._next = None
        else:
            tmp =self._head
            node._pre = None
            node._next = tmp
            tmp._pre = node
            self._head = node

    def remove(self,node):
        if node ==None:
            return 
        if self._head ==node and self._tail ==node:
            self._head = None
            self._tail = None
            return 
        if self._head ==node:
            tmp = self._head._next
            tmp._pre = None
            self._head._next = None
            self._head ==None
        elif self._tail ==node:
            tmp  = self._tail._pre
            self._tail._pre = None
            tmp.next = None
            self._tail = tmp
        else:
            node._pre._next = node._next
            node._next._pre = node._pre
            node._pre = None
            node._next = None

    def pop(self):
        # import pdb
        # pdb.set_trace()
        if self._tail ==None:
            return
        pre = self._tail._pre
        self._tail._pre = None
        if pre ==None:
            self._head = None
            self._tail = None
            return
        pre._next = None 
        self._tail = pre

def printList(obj):
    tmp = obj._head
    while tmp != None:
        print tmp._val
        tmp = tmp._next

if __name__ == '__main__':
    obj = LRUCache(10)
    obj.put(1,1)
    obj.put(2,2)
    tmp = obj.get(2)
    print tmp