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


class Client(Personne):
    def __init__(self, nom, prenom, collection):
        Personne.__init__(self, nom, prenom)
        self.collection = collection

    def inventaire(self):
        print(self.nom, self.prenom)
        for book in self.collection:
            print(book['titre'], '- quantitée : ', book['qtt'])


class Livre:
    def __init__(self, titre):
        self.titre = titre

    def print(self):
        return print(self.titre)


class Bibliotheque:
    def __init__(self, nom, catalogue):
        self.nom = nom
        self.catalogue = catalogue

    def acheterLivre(self, auteur, titre, qtt):
        for book in auteur.oeuvre:
            if book.titre == titre:
                self.catalogue.append({'titre': book.titre, 'qtt': qtt})

    def inventaire(self):
        for book in self.catalogue:
            print(self.nom)
            print(book['titre'], '- quantitée : ', book['qtt'])

    def louer(self, client, titre):
        for book in self.catalogue:
            if book['titre'] == titre:
                if (book['qtt'] - 1) >= 0:
                    client.collection.append({'titre': titre, 'qtt': 1})
                    book['qtt'] = book['qtt'] - 1

    def rendreLivre(self, client):
        for livre in self.catalogue:
            for location in client.collection:
                if location['titre'] == livre['titre']:
                    livre['qtt'] = livre['qtt'] + location['qtt']
                    location['qtt'] = 0

                if location['qtt'] == 0:
                    client.collection = []


personne = Personne('Tolkien', 'J.R.R.')
auteur = Auteur(personne.GetNom(), personne.GetPrenom())
client = Client('Mandine', 'Enzo', [])
livre = Livre('Le Seigneur des Anneaux: Le Retour Du Roi')
auteur.ecrireUnLivre(livre)
bibliotheque = Bibliotheque('J.R.R. Tolkien', [])
bibliotheque.acheterLivre(auteur, 'Le Seigneur des Anneaux: Le Retour Du Roi', 10)
bibliotheque.inventaire()
client.inventaire()
bibliotheque.louer(client, 'Le Seigneur des Anneaux: Le Retour Du Roi')
bibliotheque.inventaire()
client.inventaire()
bibliotheque.rendreLivre(client)
bibliotheque.inventaire()
client.inventaire()
