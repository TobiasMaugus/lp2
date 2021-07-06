def somaNum (a, b):
    return a+b


try:
    x = int (input ("Digite um número: "))
    y = int (input ("Digite outro número: "))
    if (somaNum(x, y) > 1000):
        raise OverflowError("A soma dos números não pode ser maior que 1000!!!")
    print (("A soma entre os números é"), (somaNum(x, y)))
except ValueError: 
    print("O valor digitado deve ser inteiro!!!")
except Exception:
    print("Ocorreu um erro inesperado!!!")