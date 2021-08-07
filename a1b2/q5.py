d={'UUU': 'Fenilanina', 'UUC': 'Fenilanina', 'UUA': 'Leucina','UUG': 'Leucina', #linha 1 coluna 1
'UCU': 'Serina', 'UCC': 'Serina', 'UCA': 'Serina', 'UCG': 'Serina', #linha 1 coluna 2
'UAU': 'Tirosina', 'UAC': 'Tirosina', 'UAA': 'Stop códon', 'UAG': 'Stop códon', #linha 1 coluna 3
'UGU': 'Cisteína', 'UGC': 'Cysteína', 'UGA': 'Stop códon', 'UGG': 'Triptofano', #linha 1 coluna 4

'CUU': 'Leucina', 'CUC': 'Leucina', 'CUA': 'Leucina', 'CUG': 'Leucina', #linha 2 coluna 1
'CCU': 'Prolina', 'CCC': 'Prolina', 'CCA': 'Prolina', 'CCG': 'Prolina', #linha 2 coluna 2
'CAU': 'Histidina', 'CAC': 'Histidina', 'CAA': 'Glutamina', 'CAG': 'Glutamina', #linha 2 coluna 3
'CGU': 'Arginina', 'CGC': 'Arginina', 'CGA': 'Arginina', 'CGG': 'Arginina', #linha 2 coluna 4

'AUU': 'Isoleucina', 'AUC': 'Isoleucina', 'AUA': 'Isoleucina', 'AUG': 'Metionina', #linha 3 coluna 1
'ACU': 'Treosina', 'ACC': 'Treosina', 'ACA': 'Treosina', 'ACG': 'Treosina', #linha 3 coluna 2
'AAU': 'Asparagina', 'AAC': 'Asparagina', 'AAA': 'Lisina', 'AAG': 'Lisina', #linha 3 coluna 3
'AGU': 'Serina', 'AGC': 'Serina', 'AGA': 'Arginina', 'AGG': 'Arginina', #linha 3 coluna 4

'GUU': 'Valina', 'GUC': 'Valina', 'GUA': 'Valina', 'GUG': 'Valina', #linha 4 coluna 1
'GCU': 'Alanina', 'GCC': 'Alanina', 'GCA': 'Alanina', 'GCG': 'Alanina', #linha 4 coluna 2
'GAU': 'Ácido Aspártico', 'GAC': 'Ácido Aspártico', 'GAA': 'Ácido Glutâmico', 'GAG': 'Ácido Glutâmico', #linha 4 coluna 3
'GGU': 'Glicina', 'GGC': 'Glicina', 'GGA': 'Glicina', 'GGG': 'Glicina', #linha 4 coluna 4
}


with open('arquivo.txt', 'r') as arq:
    arq.seek(0, 0)
    s = arq.readlines()
i=0
controle = True
contrle2 = True
while i < len(s): 
    s[i] = s[i].upper()
    s[i] = s[i].rstrip()
    print(('\n\nA fita de DNA na linha'), (i+1), ('é:'), (s[i]))
    x = s[i]
    i += 1    
    y = ''
    j = 0
    while j < len(x):
        if (x[j] == 'A'):
            y = y+'U'
        elif(x[j] == 'T'):
            y = y+'A'
        elif(x[j] == 'C'):
            y = y+'G'
        elif(x[j] == 'G'):
            y = y+'C' 
        else:
            print("Há bases não identificadas!")
            controle = False         
        j += 1  
    if(controle==True):    
        if(len(y) % 3 != 0):
            print('Há sequências de bases nitrogenadas incompletas!!')    
        else:        
            print(('A fita de RNA equivalente é:'), (y))
            print('Os aminoácidos que serão sintetizados:')
            k=0
            m=0
            while (k < len(y)):
                z=''
                m = k
                while(m <= k+2 and m<len(y) and contrle2 == True):
                    z += y[m]
                    m+=1
                k+=1
                if(z in d):
                    print((d.get(z)), ("({})".format(z)))    
    controle = True            
            
        