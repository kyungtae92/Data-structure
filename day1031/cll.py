class CLList:
    class Node:
        def __init__(self, name, link):
            self.name=name
            self.link=link

    def __init__(self):
        self.head = None
        self.tail = None 
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insertFront(self, name):
        if self.isEmpty():  # sll이 빈상태에서 첫노드 삽입 # 빈 리스트 삽입
            # t=self.Node(name, None)
            # self.head=t
            # self.head.link=t
            # self.tail=t
            self.tail = self.head = self.head.link = self.Node(name, None)
        else:   # sll에 기존 노드가 있는 상태에서 헤드 다음[첫노드]삽입
            self.head = self.Node(name, self.head)
            self.tail.link = self.head
        self.size += 1

    def insertRear(self, name, p):    # name을 p다음에 삽입
        if p == None:     # 삽입할 위치가 없다. 없는 경우, 빈 경우=>제일앞 삽입
            self.insertFront(name)
        elif p != self.tail:  # 중간삽입
            p.link = CLList.Node(name, p.link)
        else:   # 마지막노드
            self.tail = self.tail.link = CLList.Node(name, self.tail.link)
        self.size += 1

    def deleteFront(self):
        if self.isEmpty():
            raise EmptyError("Underflow")
        else:
            self.head = self.head.link
            self.tail.link=self.head
            self.size -= 1

    def deleteRear(self, p):
        if self.isEmpty():
            raise EmptyError("Underflow")
        elif p == None or self.head == self.tail:
            self.head = self.tail = None
        elif p.link != self.tail: # 중간
            p.link = p.link.link
        elif p == self.head:#처음
            self.deleteFront()
        else:   # 끝노드
            p.link = p.link.link
            self.tail = p

        self.size -= 1

    def printcll(self):
        p = self.head
        while p:
            # if p.link!=self.head:
            if p != self.tail:
                print(p.name,p, "=>", end='')
            else:
                print(p.name,p,p.link)
                print('head=', self.head, " tail=", self.tail)
                break
            p = p.link

    # def searchNode(self, trg):
    #     p = self.head
    #     while p.link!=self.head:  # size=5가정 0~4반복
    #         if trg == p.name:
    #             return p
    #         p = p.link
    #     if p.link==self.head and trg == p.name:
    #         return p
    #     return None

    def searchNode(self, trg):
        p = self.head
        while True:
            if trg == p.name:
                return p
            if p == self.tail:
                return None
            p = p.link

class EmptyError(Exception):
    pass