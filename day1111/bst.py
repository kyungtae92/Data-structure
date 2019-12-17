#Binary Seach Tree:검색 트리
class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key=key
        self.value=value
        self.left=left
        self.right=right

class BST:
    def __init__(self):
        self.root=None

    # 검색기능
    def get(self, k):
        return self.getItem(self.root, k)

    def getItem(self, n, k):
        if n==None: #빈상태
            return None;
        if n.key>k:
            return self.getItem(n.left, k)
        elif n.key<k:
            return self.getItem(n.right, k)
        else: # n.key==k 찾은 경우
            return n.value

    # 노드 삽입
    def put(self, key, value):
        self.root = self.putItem(self.root, key, value)

    def putItem(self, n, k, v):
        if n==None:
            return Node(k, v)
        if n.key > k:
            n.left=self.putItem(n.left, k, v)
        if n.key < k:
            n.right=self.putItem(n.right, k, v)
        else: # n.key == k 같은 노드가 있는 경우 삽입불가/갱신
            n.value=v
        return n

    #메뉴만들때 전체에서 최소값 삭제
    def delete_min(self): #최소값 삭제
        if self.root==None: # and n.right!=None:
            print('트리가 비었다.')
        self.root=self.del_min(self.root)

    #특정노드 아래에서 최소값 삭제
    def del_min(self, n):
        if n.left==None:
            return n.right
        n.left=self.del_min(n.left)
        return n

    def min(self): # 최소값 찾기
        if self.root==None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left==None:
            return n
        return self.minimum(n.left)

    def inorder(self, n):
        if n!=None:
            if n.left:
                self.inorder(n.left)
            print('['+str(n.key)+', '+n.value+']', end='')
            if n.right:
                self.inorder(n.right)

#메뉴에서 특정 노드 삭제
    def delete(self, k):
        self.root=self.delNode(self.root, k)

    def delNode(self, n, k):
        if n==None: #비어있어 삭제 못함
            return None
        if n.key>k:
            n.left=self.delNode(n.left, k)
        elif n.key <k:
            n.right=self.delNode(n.right, k)
        else:# == 삭제할 노드를 찾은 경우
            #오른쪽 자노드가 없거나 자노드가 없는 경우
            if n.right ==None:
                return n.left
            #외쪽 자노드가 없는 경우
            if n.left ==None:
                return n.right
            #자노드가 두개 중 오른쪽의 최소값을 삭제된 노드로 대체
            t=n
            n=self.minimum(t.right)
            n.right = self.del_min(t.right)
            n.left=t.left
            # n=self.maximum(t.left)
            # n.left = self.delete_max(t.left)
            # n.right=t.right
        return n

    # def max(self):  # 최소값 찾기
    #     if self.root == None:
    #         return None
    #     return self.maximum(self.root)
    #
    # def maximum(self, n):
    #     if n.right == None:
    #         return n
    #     return self.maximum(n.right)
    #

    # def delete_max(self): #최소값 삭제
    #     if self.root==None:
    #         print('BST가 비었다!!!')
    #         return None
    #     self.root=self.del_max(self.root)
    #
    # def del_max(self, n):
    #     if n.right==None:
    #         return n.left
    #     n.right=self.del_max(n.right)
    #     return n