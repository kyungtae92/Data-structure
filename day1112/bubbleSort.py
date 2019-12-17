# 제어된 버블소트 = selection 숙제 quick sort
data=[8,2,3,6,23,45,48,50]

cnt=0
for i in range(len(data)-1):#0~4
    sw=0
    for j in range(0, len(data)-1-i):
        cnt+=1
        if data[j]>data[j+1]:
            data[j], data[j+1]=data[j+1], data[j]
            sw=1
            # t=data[j]
            # data[j]=data[j+1]
            # data[j+1]=t
    if sw==0:break
print(data)
print("roof count:", cnt)
