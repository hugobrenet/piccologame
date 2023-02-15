def player():
    print("Bienvenue, qui veux jouer ? ")
    listofplayer = []

    for i in range(10):
        name = input("Ajouter les noms des joueurs(max 10 et stop pour arreter) : ")
        if name == "stop":
            break
        listofplayer.append(name)
    return listofplayer

def game():
    nameofplayer = player()
    print(nameofplayer)
