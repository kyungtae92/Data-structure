from collections import deque

dq = deque('data')
for node in dq:
    print(node.upper(), end='')
print()

dq.append('aaa')    #aaa
dq.appendleft('bbb')    #bbb aaa
dq.append('ccc')    #bbb aaa ccc
print(dq)
print('deque=>', dq.pop())
print('deque=>', dq.popleft())
print('deque=>', dq[-1])
print('deque=>', dq[0])
print(dq)
print('t' in dq)
dq.extend('deque')
print(dq)
dq.extendleft(reversed('python'))
print(dq)
dq.reverse()
print(dq)