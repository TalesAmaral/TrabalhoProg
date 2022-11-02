primos = []

def ehPrimo(n):
    if n%2==0: # n = 0 mod(2)
        return False # nao e primo
    for i in range(3, int(n**0.5)+1,2): # i = 3,5,7...
        if n%i == 0: # n = 0 mod(i)
            return False
    return True
def ehPalindromo(n):
    stringNum = str(n)
    return stringNum == stringNum[::-1]

lista = []
listaTemp = []
num = 11
while len(lista) !=10:
    quadrado = num**2
    inverso = int(str(quadrado)[::-1])
    if quadrado in listaTemp or inverso in listaTemp :
        lista.append(quadrado) 
    elif ehPrimo(num):
        if not ehPalindromo(quadrado):
            raiz = inverso**0.5
            if int(raiz) == raiz:
                if ehPrimo(raiz):
                    lista.append(quadrado)
                    listaTemp += [quadrado,inverso]
    num+=2
print(lista)
print(listaTemp)
print(sum(lista))









