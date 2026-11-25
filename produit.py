
class Produit:
    def __init__(self, id, nom, prix):
        self.id = id
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"Produit : ID={self.id}, Nom={self.nom}, Prix={self.prix} DH"
