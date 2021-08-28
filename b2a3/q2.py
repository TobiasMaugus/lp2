#N numero total de amigos do grupo
#M numero total de dias da reuniao
#I identificador do amigo que foi infectado por pessoas de fora do grupo
#R número da primeira reunião em que ele(I) participou infectado
#A numero total de integrantes de cada reuniao(é sempre o primeiro num da linha)
try:
    file = open("./b2a3/q2entrada.txt", "r")
    str_file  = file.readlines()
    novo_arquivo = []
    reuniao = []
    aux = []
    cont_recursiva = 0

    #FUNCAO PARA VER O NUMERO DE INFECTADOS:
    def coleta_infectado(aux, reuniao, contador_reuniao, cont_recursiva):
        aux_infectados = []
        total_infectados = []

        if (len(reuniao) != 1) and cont_recursiva != contador_reuniao:
            for i in range(0, len(aux)):
                for j in range(0, len(reuniao)):
                    if aux[i] in reuniao[j]:
                        aux_infectados.append(reuniao[j])
            for i in range(0, len(aux_infectados)):
                for j in range(0, len(aux_infectados[i])):
                    total_infectados = aux_infectados[i] + total_infectados

            aux = 0
            aux = sorted(set(total_infectados))
            cont_recursiva = cont_recursiva + 1
            return coleta_infectado(aux, reuniao, contador_reuniao, cont_recursiva)
        return aux
        
    #TRATAMENTO DE ENTRADA;
    contador_reuniao = int(str_file[0].replace("\n","").split(" ")[1])
    infectado1 = int(str_file[1].replace("\n","").split(" ")[0])
    reuniao_infectado1 = int(str_file[1].replace("\n","").split(" ")[1])-1

    for i in range(2, len(str_file)):
        novo_arquivo.append(str_file[i][1: len(str_file[i])].split(" "))
        novo_arquivo[i-2] = novo_arquivo[i-2][1:len(novo_arquivo[i-2])]
    aux_dia_reuniao = novo_arquivo[reuniao_infectado1]

    #PEGANDO INFORMAÇÕES DEPOIS QUE HOUVE INFECTADO
    for i in range(0, len(novo_arquivo)):
        reuniao.append(" ".join(novo_arquivo[i]).replace("\n","").split())
        
    aux = reuniao[reuniao_infectado1]
    reuniao = reuniao[reuniao_infectado1:len(reuniao)]

    #ANALISE DE INFECTADOS
    #print("final: ", coleta_infectado(aux, reuniao, contador_reuniao, cont_recursiva))
    var_final = coleta_infectado(aux, reuniao, contador_reuniao, cont_recursiva)
    print(len(var_final))
except FileNotFoundError:
    print("O arquivo 'q2entrada.txt' não foi encontrado!!!")    
except Exception:
    print("Ocorreu um erro inesperado!!!")
finally:    
    file.close() #FECHANDO ARQUIVO


