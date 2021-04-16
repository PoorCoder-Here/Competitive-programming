dict={}
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked:
    def __init__(self):
        self.head=None
        self.last=None
    def insert(self,data):
        if self.head==None:
            self.head=node(data)
            self.last=self.head
        else:
            self.last.next=node(data)
            self.last=self.last.next
    def delete(self,data):
        current=self.head
        if data==current.data:
            current=current.next
            self.head=current
        prev=None
        while current!=None:
              if current.data==data:
                 current=current.next
                 prev.next=current
              else:
                    prev=current
                    current=current.next
    def display(self):
        current=self.head
        while current!=None:
              print(str(current.data),end="->")
              current=current.next
    def reverse(self):
        l2=linked()
        current=self.head
        i=0
        while current!=None:
             dict[i]=current.data
             i+=1
             current=current.next
        l=len(dict)-1
        while l>=0:
              l2.insert(dict[l])
              l-=1
        l2.display()

l1=linked()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.delete(3)
l1.display()
print("\n")
l1.reverse()
                 
