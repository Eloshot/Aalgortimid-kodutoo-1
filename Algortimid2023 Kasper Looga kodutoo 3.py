a = int(input('mitmendat fibonacci arvu tahate?'))

def fibonacci(n):
    if n <= 1:
        # asukohal 0  ja asukohal 1 on arv mis vastandub selle asukohaga arvuga
        return n
    return (fibonacci(n-1) + fibonacci(n-2))
    

print(fibonacci(a)) # arvestame et jada alguspunkt ehk 0 on on indeksiga 0
    