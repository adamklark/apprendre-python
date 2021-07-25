# conding: utf-8

# les listes
liste1 = [2, 4, 8, 16, 32, 64, 128, 256]

prenoms = ["Jean", "Lea", "Nathan", "Lisa"]
print(prenoms[2])
print(prenoms[1:3])#affiche l'element l(indice 1 et 3 partant de l'indice 0

prenoms[2] = "Victor"
print(prenoms[2])

prenom = "mon prenom est Antoine"
#syntaxe: variable[index]
print(prenom[2])#affiche la valeur de l'index 2(n), présent dans la variable prenom

# les tuples

#les tuples permettent de regrouper plusieurs valeurs séparer par de virgules sans posibilité de les alterer
t1 = 1, 6, 29
t1 = "Louis", 29
t3 = (12, 20, "Lion")

#tuples vide
vide = ()

#tuples unique
unique = ("Clark")

#le deballage de sequence

t = ("Jean", 20, ["marche", "pied"])
nom, age, sport = t

#print(t)

#print(multiplication(2, 4))

#les dictionnnaires
#Un dictionnaire en python est une sorte de liste mais au lieu d'utiliser des index , on utilise des clés alphanumériques.

# declaration d'un dictionnaire
# a = {}
# ou
# b = dict()

#ajout de valeur
a = {}
a["nom"] = "Tony"
a["prenom"] = "Stark"
#print(a)

#Récupération de valeur
print(a.get('nom'))

#effacer une valeur
#del a["nom"]

