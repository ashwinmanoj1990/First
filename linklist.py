class node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def getdata(self):
        return self.val

    def setdata(self, val):
        self.val = val

    def getnext(self):
        return self.next

    def setnext(self,next):
        self.next = next

class linklist(object):
    def __init__(self,head=None):
        self.head = head
        self.count = 0

    def insert(self,data):
        newnode = node(data)
        newnode.setnext(self.head)
        self.head = newnode
        count += 1

    def find(self,val):
        

