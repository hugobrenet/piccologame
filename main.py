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
        self.geometry("300x200")
        self.liste = Listbox(self)
        
        # self.value = StringVar()
        # self.value.set("Prénom")
        # self.entree = Entry(self, textvariable=self.value, width=30)
        # self.entree.pack(pady=20)
        # self.buttonprenom = Button(self, text="Ajouter", command=addname)
        # self.buttonprenom.pack(pady=20)
        self.button = Button(self, text="Ouvrir la seconde frame", command=self.create_second_frame)
        self.button.pack(pady=20)
        

    def create_second_frame(self):
        second_window = framegame(main())
        second_window.show()
        
# def addname(self):
#     item = self.buttonprenom.get()
#     if item:
#         self.liste.insert(END,item)
#         self.buttonprenom.delete(0,END)
        
        
def main():
    r = game()
    return r


# main()
app = App()
app.mainloop()
# afficher_dictionnaire(main())
