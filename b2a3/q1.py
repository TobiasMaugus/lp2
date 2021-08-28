try:
    file = open("./b2a3/q1entrada.txt", "r")
    str_file  = file.read()

    qtd = int(str_file)

    aux = qtd+2

    if qtd <= 6:
        print("1")
    else:
        if aux%8 == 0:
            print("1")
        else:
            if qtd == 7:
                print("2")
            else:
                if aux%5 == 0:
                    print("2")
                else:
                    if qtd == 8:
                        print("3")
                    else:
                        if qtd%8 == 0:
                            print("3")
                        else:
                            print("-")
except ValueError:
    print("O arquivo possui um tipo não inteiro!!!")                            
except FileNotFoundError:
    print("O arquivo 'q1entrada.txt' não foi encontrado!!!")    
except Exception:
    print("Ocorreu um erro inesperado!!!")
finally:    
    file.close() #FECHANDO ARQUIVO