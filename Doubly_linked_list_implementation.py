class node:
    def __init__(self,data,prev):
        self.data=data
        self.next=None
        self.prev=prev
class linked:
    def __init__(self):
        self.head=None
        self.last=None
        self.before=None
    def insert(self,data):
        if self.head==None:
            prev=None
            self.head=node(data,prev)
            self.last=self.head
            self.before=prev
            print("Before:",self.before,"After:",self.head.data)
        else:
            curr=self.head
            while curr!=None:
                pre=curr
                curr=curr.next
                if curr==None:
                    prev=pre
            self.before=prev
            self.last.next=node(data,prev)
            self.last=self.last.next
            print("Before:",self.before.data,"After:",self.before.next.data)
    def dis(self):
        c=self.before
        d=self.head
        while c!=None:
            print(c.data,)
            c=c.prev
        print('None')
        print('\n')
        while d!=None:
            print(d.data)
            d=d.next
l1=linked()
l1.insert(2)
l1.insert(3)
l1.insert(7)
l1.insert(5)
