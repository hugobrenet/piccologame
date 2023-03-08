from game import (
    game,
)
from frame import (
    framegame,
)
from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Piccolo")
        self.geometry("600x500")      

        self.how_many_player = Label(self, text="Combien de joueur ?",width=30)  
        self.how_many_player.pack()

        for i in range(8):
            self.entree = Entry(self, width=30)
            self.entree.pack(pady=3)

        # self.button = Button(self, text="Ouvrir la seconde frame", command=self.create_second_frame)
        # self.button.pack(pady=20)

        self.button = Button(self, text="Ouvrir la seconde frame", command=self.addname)
        self.button.pack(pady=20)

        

    def create_second_frame(self):
        second_window = framegame(main())
        second_window.show()
        
    def addname(self):
        self.a = []
        item = self.entree.get()
        if item:
            self.a.append(item)
        print(self.a)
        
def main():
    r = game()
    return r


# main()
app = App()
app.mainloop()
# afficher_dictionnaire(main())
