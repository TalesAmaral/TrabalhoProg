def ehPrimo(n):
    if n <=1:
        return False
    if n%2==0: # n = 0 mod(2)
        return False # nao e primo
    for i in range(3, int(n**0.5)+1,2): # i = 3,5,7...
        if n%i == 0: # n = 0 mod(i)
            return False
    return True

def pegarPrimos(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return  [2,] + [p for p in range(3,n+1, 2) if prime[p]]

                                                                                                                                         

primos = pegarPrimos(1000)
maiorIntervalo = 0
for a in range(-1000, 1000):
    for b in primos:
        n = 0
        f  = n*(a+n)+b
        while  f in primos or ehPrimo(f):
            f+= n+n+1+a
            n+=1
        if n >= maiorIntervalo:
            melhorCombinacao = (a,b)
            maiorIntervalo = n
print(melhorCombinacao)
print(maiorIntervalo)
            
            
