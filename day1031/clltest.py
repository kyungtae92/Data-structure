from day1031.cll import CLList

if __name__=='__main__':
    s=CLList()
    s.insertFront('둘리')
    s.insertFront('도우너')
    s.insertFront('공실이')
    s.insertFront('고길동')    # 고길동-공실이-도우너-둘리
    s.printcll()
    p = s.searchNode('공실이')
    s.insertRear('마이콜', p)  # 고길동-공실이-마이콜-도우너-둘리
    s.printcll()
    p = s.searchNode('철수')
    s.insertRear('또치', p)   # 고길동-공실이-마이콜-도우너-둘리
    s.printcll()
    s.deleteFront()
    s.printcll()
    p = s.searchNode('공실이')
    s.deleteRear(p)
    s.printcll()
    p = s.searchNode('공실이')
    s.deleteRear(p)
    s.printcll()
    p = s.searchNode('고길동')
    s.deleteRear(p)
    s.printcll()
    # 월요일
    p = s.searchNode('고길동')
    s.deleteRear(p)
    s.printcll()

    s.deleteRear(None)
    s.printcll()