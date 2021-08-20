try:
    import csv
    with open('./b2a2/pontos.csv', encoding='utf-8', newline='') as csvfile:
        s = csv.reader(csvfile, delimiter=',') #lendo arquivo
        d= dict()

        for linha in s:
            i = 1
            v = 0
            a = []
            while(i < 6):  #colocando todas as notas em uma lista
                v = float((linha[i]))
                a.append(v)          
                i += 1
                
            menor = min(a)
            maior = max(a) 
            media = ((sum(a) - maior -menor)/3) #calculando as médias das notas de cada onda

            surfista = linha[0]
            if(surfista not in d):     #especificando qual média de onda é de qual surfista 
                d[surfista] = [media]
            else:
                d[surfista].append(media)
        
    for item in d:     
        b=(d.get(item))      
        b = (sorted(b, reverse=True))   #colocando as médias de cada surfista em ordem
        d[item] = round((b[0] + b[1]), 2) #somando apenas as duas maiores médias de cada surfista

    for item in sorted(d, key = d.get, reverse=True): 
        print((item), ('-'), (d[item])) #exibindo as notas finais de cada surfista da maior p/ menor nota

except ValueError:
    print('\nHá notas com valores não numéricos ou erro nos delimitadores no arquivo "pontos.csv"\n')
except FileNotFoundError:
    print('\nO arquivo "pontos.csv" não pôde ser encontrado!!!\n')
except Exception:
    print('\nUm erro inesperado ocorreu!!!\n')