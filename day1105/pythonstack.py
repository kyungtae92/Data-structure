def push(item):
    stack.append(item)

def pop():
    if (len(stack)!=0):
        item = stack.pop(-1)
        return item

def peak():
    if (len(stack)!=0):
        return stack[-1]

def compute(op, op1, op2):
    if op == '*':
        return op1*op2
    elif op == '/':
        return op1/op2
    elif op == '+':
        return op1+op2
    else:
        return op1-op2

def eval(exp):
    tokenlist = exp.split()    # 공백기준으로 분할 11 22 +:postfix = stack 대표적으로 수식을 postfix로 표기

    for token in tokenlist:
        if token[0] in "0123456789":
            push(int(token))
        else:
            operand2 = pop()
            operand1 = pop()
            res = compute(token, operand1, operand2)
            push(res)
    return pop()

stack = []
# print('1 2 + =>', eval('1 2 + '))
expr = input('수식입력[ex: 1 2 +]=>')
# infix => postfix변환하는 함수
print(expr,"=>", eval(expr))
