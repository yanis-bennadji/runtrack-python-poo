

class Livre:

    def __init__(self, titre , auteur, nb_page):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_page = nb_page


    def __setTitre(self):
        self.__titre = input('Entre titre du livre : ')
        return self.__titre

    def __setAuteur(self):
        self.__auteur = input("Entrer l'auteur du livre :")
        return self.__auteur

    def __setPage(self):
        while True:
            self.__nb_page = input('Entrer le nombre de page :')
            if '.' in self.__nb_page:
                print('Le nombre de page doit etre une nombre entier')
            elif self.__nb_page < str(0) or self.__nb_page.isalpha():
                print('Le nombre de page entrée possède une erreur')
            else:
                return self.__nb_page
    def getTitre(self):
        self.__setTitre()

    def getAuteur(self):
        self.__setAuteur()

    def getpage(self):
        self.__setPage()

    def AfficherTitre(self):
        return self.__titre

    def AfficherAuteur(self):
        return self.__auteur
    def afficherNombrePage(self):
        return self.__nb_page


Book = Livre('Tokyo Vice', 'Jake Adelstein', 512)
print('le Tire du livre est ', Book.AfficherTitre())
print("l'auteur du livre est ", Book.AfficherAuteur())
print("le nombre de page est de", Book.afficherNombrePage())

#modifier les valeurs
Book.getTitre()
Book.getAuteur()
Book.getpage()

print('Le Titre du livre est ', Book.AfficherTitre())
print("L'auteur du livre est ", Book.AfficherAuteur())
print("Le nombre de page est de", Book.afficherNombrePage())