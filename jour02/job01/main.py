class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return print(self.nom, self.prenom)

    def GetNom(self):
        return print(self.nom)

    def SetNom(self):
        newNom = input('Nom : ')
        self.nom = newNom
        return self.nom

    def GetPrenom(self):
        return print(self.prenom)

    def SetPrenom(self):
        newPrenom = input('Prenom : ')
        self.prenom = newPrenom
        return self.prenom


p1 = Personne("MANDINE", "Enzo")
p1.SetNom()
p1.SePresenter()
