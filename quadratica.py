def ehPrimo(n):
    if n <=1:
        return False
    if n%2==0: # n = 0 mod(2)
        return False # nao e primo
    for i in range(3, int(n**0.5)+1,2): # i = 3,5,7...
        if n%i == 0: # n = 0 mod(i)
            return False
    return True

def f(a,b,n):
    return n*(a+n)+b

intervalo = range(-1000, 1000)
melhorCombinacao = (0,0)
intervaloMelhor = 0
for a in intervalo:
    for b in intervalo:
        maiorIntervalo = 0
        qtConsecutivos = 0
        for n in range(-b,b):
            if ehPrimo(f(a,b,n)):
               qtConsecutivos +=1
            else:
                maiorIntervalo = max(maiorIntervalo,qtConsecutivos)
                qtConsecutivos = 0
    if maiorIntervalo > intervaloMelhor:
        melhorCombinacao = (a,b)
        intervaloMelhor = maiorIntervalo
print(a,b)
            
            
