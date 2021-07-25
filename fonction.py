# coding:utf-8

def message():
    print("Bienvenue")
message()

def next_year():
    global year
    print("fin de l'année", year)
    year += 1
    print("debute de l'année", year)

year = 2021
next_year()

"""def addition():
    return 5 + 5"""

"""def addition2():
    return 5 + 6"""

"""def addition3():
    return 5 + 7"""

#print("le resultat est", addition()) => sortie: le resultat est 10
#print("le resultat est", addition2()) => sortie: le resultat est 11
#print("le resultat est", addition3()) => sortie: le resultat est 12

def addition4(n):
    return 5 + n

print(addition4(50))

#ou

def additions5(n = 12):
    return 5 + n

print(additions5())



