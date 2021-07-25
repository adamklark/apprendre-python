# coding: utf-8

#boucle while

#initialise index a zéro
#tans que(conditions) i <10 j'imprime mon index est
#cherche i qui est égale a i= i + 1
#réitération jusqu'à i = 10
i = 0
while i < 10:
    print("mon index est", i)
    i = i + 1

#boucle for

m = "Bonjour  "

for lettre in m:
    print(lettre)

#initialise i à 0
#itération jusqu'a ce que soient égale a 10
for i in range(0, 10):
  print(i)

liste = [1, 5, 10, 15, 20, 25]
for i in liste:
    if i > 15:
        print("On stoppe la boucle")
        break
    print(i)



