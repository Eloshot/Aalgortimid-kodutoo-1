Stack = []
t = 0

def LIFO(a,n):
    global t
    if a == 'remove':
        if t > 0:
            t -=1
            del Stack[t]
        else:
            print('Fifo is already empty')
    elif a == 'add':
        t +=1
        Stack.insert(t,n)
        
    else:
        print ('invalid')
    return Stack

LIFO('add','toamto')
LIFO('add','potato')
LIFO('add','onion')
LIFO('remove','n')
print(Stack)