from tkinter import *

class frame():
    def iterator_next(self, dictionnaire):
        cles = list(dictionnaire.keys())
        nb_cles = len(cles)
        index_cle_actuelle = 0
        while index_cle_actuelle < nb_cles:
            # Afficher la clé et la valeur correspondante
            cle_actuelle = cles[index_cle_actuelle]
            valeur_actuelle = dictionnaire[cle_actuelle]
            
            label.config(text=f"{cle_actuelle}: {valeur_actuelle}")
        
            # Passer à l'élément suivant
            index_cle_actuelle += 1
            print(index_cle_actuelle)

            print(f"{cle_actuelle}: {valeur_actuelle}")
        print("Tous les éléments ont été affichés.")

    def iterator_back(dict):
        pass


    def framegame(self, dict):
        global frame,label
        frame = Tk()
        frame.geometry("800x400")
        frame.minsize(500,500)
        
        cles = list(dict.keys())
        index_cle_actuelle = 0
        cle_actuelle = cles[index_cle_actuelle]
        valeur_actuelle = dict[cle_actuelle]
    
        label = Label(
                frame,
                text=f"{cle_actuelle}: {valeur_actuelle}",
            )
        label.place(relx=.5,rely=.5,anchor=CENTER)
            
        back = Button(
            frame,
            text="Back",
        )
        next = Button(
            frame,
            text="Next",
            command=lambda: self.iterator_next(dict),
        )
        print(dict)
        back.pack(side="left",fill="y",ipadx=75)
        next.pack(side="right",fill="y",ipadx=75)
        
        frame.mainloop()