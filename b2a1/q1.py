try:
    with open('arquivo.txt', 'r') as arq:
        arq.seek(0, 0)
        s = arq.readlines()
    i=0

    while i < len(s): 
        s[i] = s[i].upper()
        s[i] = s[i].rstrip()
        print(('\n\nA fita de DNA na linha'), (i+1), ('é:'), (s[i]))
        print (("Adenina aparece"), (s[i].count('A')), ("vezes!"))
        print (("Timina aparece"), (s[i].count('T')), ("vezes!"))
        print (("Citosina aparece"), (s[i].count('C')), ("vezes!"))
        print (("Guanina aparece"), (s[i].count('G')), ("vezes!\n"))
        i += 1
except FileNotFoundError:
    print('"arquivo.txt" não foi encontrado!!!')
except Exception:
    print('Um erro inesperado aconteceu!!!')        

        
        

   
