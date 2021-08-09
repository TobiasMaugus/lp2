try:
    x = ["Maçã", "Banana", "Laranja", "Uva", "Carambola"]
    print ("Maçã = 0 \nBanana = 1 \nLaranja = 2 \nUva = 3\nCarambola = 4")
    y = int (input ("Digite o número da posição da lista onde está a fruta que deseja escolher: "))
    print (("Você escolheu a fruta {}!!!".format (x[y])))
except IndexError:
    print("O valor digitado não é um índice existente na lista!")
except Exception:
    print("Ocorreu um erro inesperado!!!")