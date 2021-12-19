val1 = int(input(' Digite um numero inteiro : '))
val2 = int(input(' Digite outro numero inteiro : '))

maior = []
menor = []

if val1 > val2:
    maior = val1
    menor = val2

else:
    maior = val2
    menor = val1

print(' O Maior valor é ', maior, ', O menor valor é :', menor)
mmc = 0.0

for k in range(1, maior+1):
    aux = k * menor
    if (aux % maior) == 0:
        mmc = aux

print('MMC : ', mmc)