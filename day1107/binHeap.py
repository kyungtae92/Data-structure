# 리스트 : 1,2,3,4,5,6,7,8,9
# i의 자노드: 왼쪽 i*2, 오른쪽 i*2+1
# i의 부노드: i//2

class BinHeap:
    def __init__(self, a):
        self.a = a   # a[0]는 사용하지 않는 걸로
        self.N = len(a) - 1     # a[0] 사용안하는 것 때문

    def create_Heap(self):
        for i in range(self.N//2, 0, -1):   # range(초기값, 최종값, 증감)
            self.downheap(i)

    def insert(self, key):
        self.N += 1     # 리스트에 추가해서 개수 증가
        self.a.append(key)
        self.upheap(self.N)     # 마지막에 추가되었으므로 올라가면서 heap을 재구성

    def delete_min(self):   # 루트에 있는 값 삭제
        if self.N == 0:     # 힙이 빈 상태
            print('힙이 비었다. 삭제 불가!!!')
            return None
        min = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]   # a, b = 1, 2  첫노드와 마지막노드 교환
        del self.a[-1]
        self.N -= 1
        self.downheap(1)
        return min

    def downheap(self, i):
        while 2*i <= self.N:     # i의 왼쪽자식이 힙에 있을 동안 반복
            k = 2*i     # k가 왼쪽자식임을 의미
            if k < self.N and self.a[k+1][0] > self.a[k+1][0]:
                # a[k][0]: 키값, a[k][1]: 데이터 a는 a[[],[10, 'apple'],[12, 'orange'],...]
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]     # 통째로 바꾼다는 의미
            # self.a[i][0] , self.a[k][0] = self.a[k][0] , self.a[i][0]
            # self.a[i][1] , self.a[k][1] = self.a[k][1] , self.a[i][1]
            i = k  # 자식이 낮은 값이라 부모와 바뀌었으믄로 k위치에 i가 이동했으므로 i에 k값을 할당

        while i > 1 and self.a[i//2][0] > self.a[i][0]:     # i가 루트가 아니고 i가 부모보다 부모보다 작을 동안 반복
            self.a[i // 2], self.a[i] = self.a[i], self.a[i//2]    # 부모와 자식의 교환
            i = i//2    # 부모와 교환되었으므로 비교 위치i를 부모로 변경

    def printHeap(self):
        print('MinHeap=', end='')
        for i in range(1, self.N+1):
            print('[%d:%s]' % (self.a[i][0], self.a[i][1]), end='')
        print()
        print('Heap Size:', self.N)


