class Node:
    def __init__(self, item, link):
        self.item = item
        self.link = link

def push(item):
    global top
    global size
    # if max <= size:
    #     print("overflow!!!")
    #     return
    top = Node(item, top)
    size += 1

def pop():
    global top
    global size
    if size != 0:
        top_item = top.item
        top = top.link
        size -= 1
        return top_item
    else:
        print("underflow발생, 출력불가")

def peak():
    if size != 0:
        return top.item
    else:
        print("underflow발생, 없음")
        return None

def printStack():
    print("Top ->\t", end='')
    p = top
    while p:
        if p.link != None:
            print(p.item, "=>", end ="")
        else:
            print(p.item)
        p = p.link

# max = 10
top = None
size = 0
