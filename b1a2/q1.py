try: 
    x = int( input ( "Entre com um numero: " ) )
    y = int( input ( "Entre com outro numero: " ) )
    print( x, '/', y, '=', x/y )
except ValueError:
    print ("O valor digitado deve ser inteiro!!!")
except ZeroDivisionError:    
    print ("O valor do divisor deve ser diferente de zero!!!")
except Exception:
    print("Ocorreu um erro inesperado!!!")
