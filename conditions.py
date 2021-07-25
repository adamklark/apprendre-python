# coding: utf-8

# les conditions

indentifiant = "Lucs"
mots_de_passe = "password1234"

print("interface de connexion")

user_id = input("Entrez votre identifiant: ")
user_password = input("entrez votre mots de pass:")

if user_password == mots_de_passe:
    print("Vous êtes connectés, bienvenue", user_id)
print("je suis pas dans la condition")