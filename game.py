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


def game(player):
    import random
    nameofplayer = player
    random.shuffle(nameofplayer)
    questionforplayer = question()

    dict = {}
    for name in nameofplayer:
        for request in questionforplayer:
            dict[name] = request
            questionforplayer.remove(request)
            break
  
    return dict

    

    


