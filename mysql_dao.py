
import mysql.connector
from produit import Produit
from client import Client


class MySQLDAO:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        cursor = self.conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS boutique")
        cursor.close()
        self.conn.close()

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="boutique"
        )

        self.creer_tables()

    def creer_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(100) NOT NULL,
                prix FLOAT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL UNIQUE
            )
        """)

        self.conn.commit()
        cursor.close()

    def ajouter_produit(self, produit):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO produits (nom, prix) VALUES (%s, %s)",
                (produit.nom, produit.prix)
            )
            self.conn.commit()
            print("Produit ajouté avec succès.")
            cursor.close()

        except mysql.connector.Error as e:
            print("Erreur :", e)

    def lister_produits(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM produits")
        produits = cursor.fetchall()

        for p in produits:
            print(Produit(p[0], p[1], p[2]))

        cursor.close()

    def ajouter_client(self, client):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO clients (nom, email) VALUES (%s, %s)",
                (client.nom, client.email)
            )
            self.conn.commit()
            print("Client ajouté avec succès.")
            cursor.close()

        except mysql.connector.Error as e:
            print("Erreur :", e)

    def lister_clients(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()

        for c in clients:
            print(Client(c[0], c[1], c[2]))

        cursor.close()

    def rechercher_client(self, email):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM clients WHERE email = %s",
            (email,)
        )

        c = cursor.fetchone()

        if c:
            print(Client(c[0], c[1], c[2]))
        else:
            print("Client introuvable.")

        cursor.close()

    def modifier_prix(self, id, nouveau_prix):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE produits SET prix = %s WHERE id = %s",
                (nouveau_prix, id)
            )
            self.conn.commit()

            if cursor.rowcount > 0:
                print("Prix modifié avec succès.")
            else:
                print("Produit introuvable.")

            cursor.close()

        except mysql.connector.Error as e:
            print("Erreur :", e)

    def fermer(self):
        self.conn.close()
