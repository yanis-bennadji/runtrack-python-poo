class Personne():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print("Je suis", (self.prenom), (self.nom))

nom1 = Personne ("Doe", "John")
nom2 = Personne ("Dupond", "Jean")
nom1.SePresenter()
nom2.SePresenter()
