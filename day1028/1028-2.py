#Lambda식 : 반복문을 단축
# a = [1, 5, 4, 6, 8, 11, 3, 10]
#
# even = list(filter(lambda x:(x%2==0), a))
# print(even)
# tentimes = list(map(lambda x:x*10, a))
# print(tentimes)

# b = [[0,1,8],[7,9,3],[9,10,1],[2,3,5]]
# b.sort()
# print(b)
# b.sort(key=lambda x:x[2])
# print(b)

# 수행시간 체크(현재시간 - 시작시간)
import random
import time

random.seed(time.time())
startTime = time.time()

a = []
for i in range(1000):
    for j in range(10000):
        b = []
        b.append(random.randint(1,1000))
    a.append(b)
print("---%s seconds---"%(time.time()-startTime))

