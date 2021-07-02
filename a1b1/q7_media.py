x = []
y = 1
while (y != 0):
    y=0
    y = int(input ('Informe um número: '))
    if(y != 0):
        x.append(y) 

print ('A média dos números digitados é', (sum(x)/len(x)))
