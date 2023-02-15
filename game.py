def player():
    print("Bienvenue, qui veux jouer ? ")
    listofplayer = []
    for i in range(10):
        name = input("Ajouter les noms des joueurs(max 10 et stop pour arreter) : ")
        if name == "stop":
            break
        listofplayer.append(name)
    return listofplayer


def question():
    question = [
        "Comment ça va ?",
        "La capital de la France ?",
        "Qu'elle est ton prénom ?",
        "Quel age tu as ?",
        "Tu es à la fac ?",
        "Tu utilises un ordinateur ?"
    ]
    return question


def game():
    import random
    nameofplayer = player()
    random.shuffle(nameofplayer)
    questionforplayer = question()
    random.shuffle(questionforplayer)

    dict = {}
    for name in nameofplayer:
        for request in questionforplayer:
            dict[name] = request
            questionforplayer.remove(request)
            break
    print(dict)

