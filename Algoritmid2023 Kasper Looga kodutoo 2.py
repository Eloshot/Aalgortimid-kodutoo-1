Stack = []
t = 0 # t on inex

def LIFO(a,n): # a soovib teada kas me lisame või eemaldame ja n on mida lisame kui lisame
    global t
    if a == 'remove': # kui a on remove siis eemalda
        if t > 0:
            t -=1 
            del Stack[t] # eemaldame viimati lisatud asja
        else: #stackis ei ole midagi
            print('Fifo is already empty')
    elif a == 'add':
        
        Stack.insert(t,n) # lisame stacki t asukohale n elemendi
        t +=1
        
    else:
        print ('invalid') # ebasobiv vastus
    return 

# test
LIFO('add','toamto')
print(Stack)
LIFO('add','potato')
print(Stack)
LIFO('add','onion')
print(Stack)
LIFO('remove',None)
print(Stack)