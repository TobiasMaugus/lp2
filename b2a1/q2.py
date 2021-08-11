try:
    with open('./b2a1/arquivo.txt', 'r') as arq:
        arq.seek(0, 0)
        s = arq.readlines()
    i=0

    while i < len(s): 
        s[i] = s[i].upper()
        s[i] = s[i].rstrip()
        print(('\n\nA fita de DNA na linha'), (i+1), ('é:'), (s[i]))
        x = s[i]
        i += 1    
        y = ''
        j = 0
        controle = True
        while j < len(x):
            if (x[j] == 'A'):
                y = y+'T'
            elif(x[j] == 'T'):
                y = y+'A'
            elif(x[j] == 'C'):
                y = y+'G'
            elif(x[j] == 'G'):
                y = y+'C'
            else:
                print('Há bases não identificadas!!!')
                controle = False       
            j += 1
        if (controle == True):
            print(('A fita suplementar é:'), (y))
except FileNotFoundError:
    print('"arquivo.txt" não foi encontrado!!!')
except Exception:
    print('Um erro inesperado aconteceu!!!')  
      
    


    
       