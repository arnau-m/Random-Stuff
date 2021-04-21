from random import randrange
from fibonacci import fibonacci

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

presupost = 20
fibo = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
i = 0   

for f in range(20):
    aposta = fibo[i]
    resultat = randrange(2)
    presupost = presupost - aposta
    if resultat == 0:
        benefici = aposta * 2
        presupost = presupost + benefici
        if i == 0:
            i = i
        elif i == 1:
            i = 0
        else:
            i = i - 2
        print(f'{bcolors.OKGREEN}Has GUANYAT {aposta}€ ({presupost})')
    else:
        i = i + 1
        print(f'{bcolors.FAIL}Has PERDUT {aposta}€ ({presupost})')
    if presupost < 0:
        print('Bancarotta')
        break
