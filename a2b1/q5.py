try:
    x = int (input ("Informe um número: "))
    if ((x <= 2)):
        raise ValueError("O valor deve ser um número natural maior que 2!!!")
    else:
        l = []
        i = 0
        while i < x:
            j = 1
            c = 0
            while (j <= i):
                if ((i % j) == 0):
                    c=c+1
                j=j+1
            if (c == 2): 
                l.append(i)
            i=i+1
        print("A lista de números primos existentes entre 1 e {} é: {}".format(x, l))
except ValueError:
    print("O valor deve ser um número natural maior que 2!!!")
except Exception:
    print("Ocorreu um erro inesperado!!!")

