class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return print(self.nom, self.prenom)

    def GetNom(self):
        return self.nom

    def SetNom(self):
        newNom = input('Nom : ')
        self.nom = newNom
        return self.nom

    def GetPrenom(self):
        return self.prenom

    def SetPrenom(self):
        newPrenom = input('Prenom : ')
        self.prenom = newPrenom
        return self.prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        Personne.__init__(self, nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        for book in self.oeuvre:
            book.print()

    def ecrireUnLivre(self, livre):
        return self.oeuvre.append(livre)


class Livre:
    def __init__(self, titre):
        self.titre = titre

    def print(self):
        return print(self.titre)


personne = Personne('MANDINE', 'Enzo')
auteur = Auteur(personne.GetNom(), personne.GetPrenom())

auteur.ecrireUnLivre(Livre('Le Seigneur des Anneaux: Le Retour Du Roi'))
auteur.listerOeuvre()
