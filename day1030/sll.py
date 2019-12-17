class SLList:
    class Node:
        def __init__(self, name, link):
            self.name=name
            self.link=link

    def __init__(self):
        self.head=None
        self.size=0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size==0

    def insertFront(self, name):
        if self.isEmpty():#sll이 빈상태에서 첫노드 삽입
            self.head=self.Node(name, None)
        else:#sll에 기존 노드가 있는 상태에서 헤드 다음[첫노드]삽입
            self.head=self.Node(name,self.head)
        self.size+=1

    def insertRear(self,name,p):#name을 p다음에 삽입
        if p==None:#삽입할 위치가 없다. 없는 경우, 빈 경우=>제일앞 삽입
            self.insertFront(name)
        else:#삽입 위치가 있다.
            p.link=SLList.Node(name,p.link)
        self.size+=1

    def deleteFront(self):
        if self.isEmpty():
            raise EmptyError("Underflow")
        else:
            self.head = self.head.link
            self.size-=1

    def deleteRear(self, p):
        if self.isEmpty():
            raise EmptyError("Underflow")
        p.link=p.link.link
        self.size-=1

    def search(self, trg):
        p=self.head
        t=None
        for i in range(self.size):#size=5가정 0~4반복
            if trg==p.name:
                t = i
            p=p.link
        return t

    def searchNode(self, trg):
        p = self.head
        while p:  # size=5가정 0~4반복
            if trg == p.name:
                return p
            p = p.link
        return None

    def printsll(self):
        p=self.head
        while p:
            if p.link!=None:
                print(p.name,"=>", end='')
            else:
                print(p.name)
            p=p.link

class EmptyError(Exception):
    pass