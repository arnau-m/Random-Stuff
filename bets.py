from random import randrange

times = int(input('How many times do you want to throw the coin? '))
bet = int(input('How much to you want to bet? Remember that I will bet 1,5 times yours. '))

face = 0
cross = 0

for i in range(times):
    x = randrange(2)
    if x == 0:
        face = face + 1
    else:
        cross = cross + 1
print(f'Face (you) won {face} times')
print(f'Cross (me) won {cross} times')


youBet = int(face) * int(bet)
myBet = int(cross) * (bet * 1.5)
benefits = myBet - youBet
print(f'You have won {benefits}€')