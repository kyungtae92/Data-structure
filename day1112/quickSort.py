def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot-1)
        qsort(a, pivot+1, high)
        
def partition(a, pivot, high):
    i = pivot+1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:  # 아직 확인하지 않은 데이터가 있고, 피봇보다 큰 경우까지 반복
            i += 1  # low부터 츨발해서 피봇보다 큰 값이 있을 때까지 이동
        while j > pivot and a[j] > a[pivot]:
            j -= 1

        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    a[pivot], a[j] = a[j], a[pivot]
    return j

a = [52, 58, 42, 36, 54, 78, 96, 2, 570, 45 , 63, 10, 23, 65, 67, 80, 100,]
print('정렬전:')
print(a)
qsort(a, 0, len(a)-1)
print('정렬후:')
print(a)
