class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def __setLongueur(self):
        self.longueur = input('entrer une longueur: ')
        return self.longueur

    def getLongueur(self):
        self.__setLongueur()

    def __setLargeur(self):
        self.largeur = input('Entrer une largeur : ')
        return self.largeur

    def getLargeur(self):
        self.__setLargeur()

    def AfficherLongueur(self):
        return self.longueur

    def AfficherLargeur(self):
        return self.largeur



rectangle = Rectangle(10,5)
#afficher les valeur non modifié
print('la longeur est de',rectangle.AfficherLongueur())
print('La largeur est de', rectangle.AfficherLargeur())

#modifier les caleur
rectangle.getLongueur()
rectangle.getLargeur()
print('la longeur est de',rectangle.AfficherLongueur())
print('La largeur est de', rectangle.AfficherLargeur())