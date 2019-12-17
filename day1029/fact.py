# factorial 함수 재귀적호출의 예
# def fact(n):
#     if n <= 1:      # 재귀적 함수의 종료조건
#         return 1
#     else:
#         return n*fact(n-1)      # 재귀적 호출
#
# indata = int(input('숫자입력'))
# print('fact(%d)='%(5), fact(5)) # 5*4*3*2*1     #print('fact(%d)='%(indata), fact(indata))

# def fact(n):      # 위에꺼랑 같음
#     res = 1
#     for i in range(1, n+1):
#         res*=i
#
#     return res
#
# indata = int(input('숫자입력'))
# print('fact(%d)='%(indata), fact(indata))



# 재귀적 호출을 통한 피보나치 수열 생성
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-2) + fibo(n-1) # 2-> fibo(1)+fibo(0) = 1이 리턴
#     # fibo(4) = fibo(3)[=fibo(2)[=fibo(1) + fibo(0)] + fibo(1)] + fibo(2)[=fibo(1) + fibo(0)]_
#     # 최종적으로 1+0+1+1+0=3
# indata = int(input('숫자입력'))
# print('fibo(%d)=>'%(indata), end='')
# for i in range(indata): # idata=5 -> range범위 0~4(5번)
#     if i == indata-1:
#         print('f(%d)' % (i) + '=' + str(fibo(i)))
#     else:
#         print('f(%d)'%(i)+'='+str(fibo(i))+',', end='')

# 함수를 통한 피보나치 수열 생성
# f = []
# def fibo(n):
#     for i in range(n):
#         if i == 0:
#             f.append(0)
#         elif i == 1:
#             f.append(1)
#         else:
#             f.append(f[i-1] + f[i-2])
#
# indata = int(input('숫자입력'))
# print('fibo(%d)=>'%(indata), end='')
# fibo(indata)
# print(f) # 간편하게 하려면 밑에꺼 다 날려도 됨
# for i in range(indata):
#     if i == indata:
#         print('f(%d)' % (i) + '=' + str(f[i]))
#     else:
#         print('f(%d)' % (i) + '=' + str(f[i]) + ',', end='')


# 10진수 입력 받아서 2진수 출력
# def dec2bin(n):
#     if n == 0:
#         return
#     dec2bin(n//2)
#     print(n%2, end='')
#     return
#
# indata = int(input('숫자입력'))
# print('dec(%d)=>bin('%(indata), end='')
# dec2bin(indata)
# print(')')

# 하노이탑 알고리즘
def move(disk, src, tar, tmp):
    if disk == 1:
        print('Move Disk:', disk, 'from', src, 'to', tar)
    else:
        move(disk-1, src, tmp, tar)
        print('Move Disk:', disk, 'from', src, 'to', tar)
        move(disk-1, tmp, tar, src)

print(move(3,'A','B','C'))
