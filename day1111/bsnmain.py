from d1111.bst import *

#bst생성
t=BST()
#노드 삽입
t.put(90,'수박')
t.put(80,'배')
t.put(70,'멜론')
t.put(50,'라임')
t.put(60,'망고')
t.put(20,'체리')
t.put(30,'포도')
t.put(35,'오렌지')
t.put(10,'귤')
t.put(15,'바나나')
t.put(45,'레몬')
t.put(40,'키위')
#inorder 출력
t.inorder(t.root)
print()
#노드 삭제-중간노드 삭제
t.delete(40)
t.inorder(t.root)
#찾기기능
print()
print(t.get(30))
#최소값 출력
min=t.min()
print(min.key, min.value)