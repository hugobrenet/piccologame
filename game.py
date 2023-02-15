def player():
    print("Bienvenue dans le piccolo, qui veux jouer ? ")
    listofplayer = []
    try:
        for i in range(10):
            i = i + 1
            name = input("Ajouter les noms des joueurs(max 10 et stop pour arreter) : ")
            if name == "stop":
                break
            listofplayer.append(name)
    except ValueError as error:
        print("Veuillez ne pas mettre de nombre. {}".format(error))
    
    print("Les joueurs sont {}".format(listofplayer))
        

    


if __name__=="__main__":
    player()
