# Performanse racunarskih sistema, ETF Banja Luka
# Laboratorija broj 4
# Zelimir Maletic 11125/18
# 13/04/2020

import random
import math
import timeit

numberOfCycles = 0
numberOfDigits = 0
userChoice = ''

print("+------------------Generisanje broja Pi------------------+")
print("| Izaberite jednu od opcija:                             |")
print("|   a) broj generisanih vrijednosti                      |")
print("|   b) broj tacnih cifara broja Pi                       |")
while(not(userChoice=='a' or userChoice=='b')):
    userChoice = input("|>>")
print("|--------------------------------------------------------|")

if(userChoice == 'a'):
    numberOfCycles = int(input("Broj slucajno generisanih vrijednosti: "))
    dotsInCircle = 0
    print("Generisanje broja Pi moze da potraje...")
    start_time = timeit.default_timer()
    for i in range(0,numberOfCycles):
        x = random.random()
        y = random.random()
        if(math.sqrt(x*x + y*y)<=1):
            dotsInCircle+=1
    elapsed = timeit.default_timer() - start_time
    print("=================================================")
    print("Vrijeme izvrsavanja programa: " + str(elapsed))
    print("Vrijednost broja Pi iznosi: " + str((dotsInCircle/float(numberOfCycles))*4.0))
    print("Tacna vrijednost broja Pi: " + str(math.pi))
else:
    numberOfDigits = int(input("Broj tacnih cifara broja Pi: "))
    dotsInCircle = 0
    calculatedPiValue = 3
    numberOfCycles = 10
    criteria = 1/math.pow(10,numberOfDigits+1)
    print("Generisanje broja Pi moze da potraje...")
    error = 1
    while error>criteria:
            for i in range(0,numberOfCycles):
                x = random.random()
                y = random.random()
                if(math.sqrt(x*x + y*y)<=1):
                    dotsInCircle+=1
            calculatedPiValue = (dotsInCircle/float(numberOfCycles))*4.0
            dotsInCircle = 0
            error = abs(math.pi-calculatedPiValue)
            numberOfCycles+=100
    print("=================================================")
    print("Potreban broj iteracija: " + str(numberOfCycles))
    print("Vrijednost broja Pi: " + str(calculatedPiValue))
    print("Tacna vrijednost broja Pi: " + str(math.pi))
print("+------------------Zelimir Maletic, 2020------------------+")
