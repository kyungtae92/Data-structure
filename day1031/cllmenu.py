from day1031.cll import CLList

def menu():
    print(' === Circular Linked List MENU ===')
    print(' 1. insertFront')
    print(' 2. insertRear')
    print(' 3. delete')
    # print(' 4. deleteRear')
    print(' 5. Search')
    print(' 6. print list')
    print(' 0. exit')
    print(' =================================')
    print(' select:', end='')

if __name__ == '__main__':
    s = CLList() # 리스트 생성
    while True:# 입력값이 0이 아닐때 까지 반복 while True:
        menu()
        sel= int(input())# 입력 sel
        if sel==1:# 선택 if~elif~else
            data=input('삽입 데이터 입력:')
            s.insertFront(data)
        elif sel == 2:
            data = input('삽입 데이터 입력:')
            pos = input('삽입 위치 선택:')
            p=s.searchNode(pos)
            # print(p.name)
            s.insertRear(data, p[1])
        elif sel==3:
            data = input('삭제할 사람 입력 :')
            s.delete(data)
        elif sel==5:
            data = input('찾을 사람 입력 :')
            p = s.searchNode(data)
            print('찾은 사람은', p[1].name+'입니다.')
        elif sel==6:
            s.printList()
        elif sel==0:
            print("사용이 끝났어요!!! 바이~~")
            break
        else:
            print("선택오류 0~6사이를 입력하시오.")
            continue
