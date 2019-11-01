"""Cows and Bulls game"""

import random as r

r.seed();
cows=0
bulls=0
number = str(r.randint(1000,9999));

while True:
    guess=input("Guess")
    for cifra in guess:
        if cifra is number:
            if number.index(cifra) == guess.index(cifra):
                bulls+=1;
            else:
                cows+=1;
        if bulls==4:
            print("You win.GG")
            break
        bulls=0
        cows=0
