y = int (input ('Informe o número do termo da sequencia de Fibonacci: '))

x1 = 0
x2 = 1
i = 0
while (i < y):
    x3 = (x1+x2)
    x1 = x2
    x2 = x3
    i = i+1

print (('O termo'), (y), ('da sequência é'), (x1))     