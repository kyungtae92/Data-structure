from day1030.sll import SLList

if __name__ == '__main__':
    s=SLList()
    s.insertFront('둘리')
    s.insertFront('도우너')
    s.insertFront('공실이')
    s.insertFront('고길동')    # 고길동-공실이-도우너-둘리
    s.printsll()
    p=s.searchNode('공실이')
    s.insertRear('마이콜', p)  # 고길동-공실이-마이콜-도우너-둘리
    s.printsll()
    p=s.searchNode('둘리')
    s.insertRear('영희', p)   # 고길동-공실이-마이콜-도우너-둘리-
    s.printsll()
    s.deleteFront()
    s.printsll()
    p = s.searchNode('마이콜')
    s.deleteRear(p)
    s.printsll()


