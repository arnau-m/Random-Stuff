#Exercici PAU 2015, calcular quins nombres sumats entre ells proporcionen un resultat divisor de 3

print('Si vols calcular totes les possibles combinacions prem 1')
print('Si vols calcular només les combinacions amb nombres múltiples de 3 prem 2')
print('Si vols calcular només les combinacions amb nombres NO múltiples de 3 prem 3')
resposta = int(input())
x = int(input('Fins quin número vols treballar?'))+1
numbers = []
for i in range(x):
    numbers.append(i)
resultlist = []


def tots():   
    for number in numbers:
        for i in range(x):
            if (number+i)%3 == 0:
                result = number, i
                if (result not in resultlist):
                    print(result)
                result2 = i, number 
                resultlist.append(result2)

def multiples():
    for number in numbers:
        for i in range(x):
            if (number+i)%3 == 0 and number%3 == 0 and i%3 == 0:
                result = number, i
                if (result not in resultlist):
                    print(result)
                result2 = i, number 
                resultlist.append(result2)

def noMultiples():
    for number in numbers:
        for i in range(x):
            if (number+i)%3 == 0 and number%3 != 0 and i%3 != 0:
                result = number, i
                if (result not in resultlist):
                    print(result)
                result2 = i, number 
                resultlist.append(result2)
if resposta == 1:
    tots()
elif resposta == 2:
    multiples()
elif resposta == 3:
    noMultiples()
else:
    print('Torna a probar-ho')