# coding: utf-8

class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur:", pseudo, "point de vie:",health, "attaque:", attack )

player1 = Player("Jean", 20, 4)
player2 = Player("Lucs", 25, 3)


