try:
    x = int (input ("Digite um número: "))
    i = x
    y = x
    if (x<0):
        raise ValueError("O valor deve ser um número natural!!!")
    elif (x == 0):
        print("O fatorial de 0 é 1!!!")        
    else:
        while (i > 1):
            i = i-1
            x = x*i
        print("O fatorial de {} é {}!!!".format(y, x))
except ValueError:
    print("O valor deve ser um número natural!!!")
except Exception:
    print("Ocorreu um erro inesperado!!!")