class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item    # 멤버변수
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self, n): # n에 root가 # 출력 왼 오
        if n != None:
            print(str(n.item), ' ', end='')
            if n.left != None:
                self.preOrder(n.left)
            if n.right != None:
                self.preOrder(n.right)

    def inOrder(self, n): # n에 root가 # 왼 출력 오
        if n != None:
            if n.left != None:
                self.inOrder(n.left)
            print(str(n.item), ' ', end='')
            if n.right != None:
                self.inOrder(n.right)

    def postOrder(self, n):  # n에 root가 # 왼 오 출력
        if n != None:
            if n.left != None:
                self.postOrder(n.left)
            if n.right != None:
                self.postOrder(n.right)
            print(str(n.item), ' ', end='')

    def levelOrder(self, root):
        q = []
        q.append(root)
        while len(q) != 0:  # 큐가 비어 있지 않을 동안 반복
            t = q.pop(0)
            print(str(t.item), ' ', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

    def height(self, root): # depth
        if root == None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    def size(self, root):
        if root == None:
            return 0
        else:
            return 1 + self.size(root.left) + self.size(root.right)

    def copyTree(self, n):
        if n == None:
            return None
        else:
            left = self.copyTree(n.left)
            right = self.copyTree(n.right)
            return Node(n.item, left, right)

    def isEqual(self, n, m):
        if n == None and m == None:
            return n == m
        if n.item != m.item:
            return False
        return (self.isEqual(n.left, m.left)) and (self.isEqual(n.right, m.right))






