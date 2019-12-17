class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

def enQue(item):
    global front
    global rear
    global size
    new = Node(item, None)
    if size == 0:
        front = rear = new
    else:
        rear.next = new
        rear = new
    size += 1

def deQue():
    global front
    global rear
    global size
    res = None

    if size != 0:
        res = front.item
        front = front.link.next
        size -= 1
        if size == 0:
            rear = None
    else:
        print("underflow!!! 출력불가")
    return res

def printQue():
    print("front <=\t", end='')
    p = front
    while p:
        if size == 0:
            print("Queue is Empty!!!")
            break
        if p.next != None:
            print(p.item, "<=", end="")
        else:
            print(p.item, '<= rear')
        p = p.next

front = rear = None
size = 0

enQue('aaa')
enQue('bbb')
enQue('ccc')
printQue()
res = deQue()
print('deQue data=', res)
printQue()