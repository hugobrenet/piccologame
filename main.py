from game import (
    game,
)
from frame import (
    framegame,
)
from tkinter import *
list_entry = []
list_of_name = []
class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Piccolo")
        self.geometry("600x500")      

        self.how_many_player = Label(self, text="Combien de joueur ?",width=30)  
        self.how_many_player.pack()
        self.how_many_player_entry = Entry(self, width=30)
        self.how_many_player_entry.pack()

        self.button = Button(self, text="Ajouter", command=self.ajouterchamp)
        self.button.pack(pady=20)
        # for i in range(8):
        #     self.entree = Entry(self, width=30)
        #     self.entree.pack(pady=3)

        # self.button = Button(self, text="Ouvrir la seconde frame", command=self.create_second_frame)
        # self.button.pack(pady=20)

        self.button = Button(self, text="Jouer", command=self.addname)
        self.button.pack(pady=20)

    def ajouterchamp(self):
        recup = int(self.how_many_player_entry.get())
        for i in range(recup):
            var = Entry(self)
            list_entry.append(var)
            var.pack()

        
    def addname(self):
        for i in list_entry:
            recup = (i.get())
            list_of_name.append(recup)
        print(list_of_name)
        second_window = framegame(game(list_of_name))
        second_window.show()

        
def main():
    r = game()
    return r


# main()
app = App()
app.mainloop()
# afficher_dictionnaire(main())
