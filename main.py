
from produit import Produit
from client import Client
from sqlite_dao import SQLiteDAO
from mysql_dao import MySQLDAO


print("===== GESTION DE BOUTIQUE =====")
print("1. SQLite")
print("2. MySQL")

choix = input("Choisir la base de données : ")

dao = None

try:
    if choix == "1":
        dao = SQLiteDAO()
        print("Connexion SQLite réussie.")

    elif choix == "2":
        dao = MySQLDAO()
        print("Connexion MySQL réussie.")

    else:
        print("Choix invalide.")
        exit()

    while True:

        print("\n===== MENU PRINCIPAL =====")
        print("1. Ajouter un produit")
        print("2. Lister les produits")
        print("3. Ajouter un client")
        print("4. Lister les clients")
        print("5. Rechercher un client par email")
        print("6. Modifier le prix d'un produit")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            nom = input("Nom du produit : ")
            prix = float(input("Prix du produit : "))

            produit = Produit(None, nom, prix)
            dao.ajouter_produit(produit)

        elif choix == "2":
            dao.lister_produits()

        elif choix == "3":
            nom = input("Nom du client : ")
            email = input("Email du client : ")

            client = Client(None, nom, email)
            dao.ajouter_client(client)

        elif choix == "4":
            dao.lister_clients()

        elif choix == "5":
            email = input("Email à rechercher : ")
            dao.rechercher_client(email)

        elif choix == "6":
            id = int(input("ID du produit : "))
            prix = float(input("Nouveau prix : "))

            dao.modifier_prix(id, prix)

        elif choix == "0":
            print("Fin du programme.")
            break

        else:
            print("Choix invalide.")

except Exception as e:
    print("Erreur de connexion ou d'exécution :", e)

finally:
    if dao is not None:
        dao.fermer()
