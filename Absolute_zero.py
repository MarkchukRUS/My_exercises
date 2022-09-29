primer = input().split(' ')

a = int(0)
b = int(0)

n = 1
for i in range(len(primer)):
    if primer[int(i)] == '/':
        if n == 1:
            a = (int(primer[int(i - 1)]) / int(primer[int(i + 1)]))
            n = 10
        else:
            a = int((int(a) / int(primer[i+1])))

    if primer[int(i)] == '*':
        if n == 1:
            a = (int(primer[int(i - 1)]) * int(primer[int(i + 1)]))
            n = 10
        else:
            a = int((int(a) * int(primer[i+1])))

    if primer[int(i)] == '+':
        if n == 1:
            a = (int(primer[int(i - 1)]) + int(primer[int(i + 1)]))
            n = 10
        else:
            a = int((int(a) + int(primer[i+1])))

    if primer[int(i)] == '-':
        if n == 1:
            a = (int(primer[int(i - 1)]) - int(primer[int(i + 1)]))
            n = 10
        else:
            a = int((int(a) - int(primer[i+1])))



print(a)
