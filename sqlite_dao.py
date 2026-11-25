
import sqlite3
from produit import Produit
from client import Client


class SQLiteDAO:

    def __init__(self):
        self.conn = sqlite3.connect("boutique.db")
        self.creer_tables()

    def creer_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prix REAL NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)

        self.conn.commit()

    def ajouter_produit(self, produit):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO produits (nom, prix) VALUES (?, ?)",
                (produit.nom, produit.prix)
            )
            self.conn.commit()
            print("Produit ajouté avec succès.")

        except sqlite3.Error as e:
            print("Erreur :", e)

    def lister_produits(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM produits")

        produits = cursor.fetchall()

        for p in produits:
            print(Produit(p[0], p[1], p[2]))

    def ajouter_client(self, client):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO clients (nom, email) VALUES (?, ?)",
                (client.nom, client.email)
            )
            self.conn.commit()
            print("Client ajouté avec succès.")

        except sqlite3.Error as e:
            print("Erreur :", e)

    def lister_clients(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clients")

        clients = cursor.fetchall()

        for c in clients:
            print(Client(c[0], c[1], c[2]))

    def rechercher_client(self, email):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM clients WHERE email = ?",
            (email,)
        )

        c = cursor.fetchone()

        if c:
            print(Client(c[0], c[1], c[2]))
        else:
            print("Client introuvable.")

    def modifier_prix(self, id, nouveau_prix):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE produits SET prix = ? WHERE id = ?",
                (nouveau_prix, id)
            )
            self.conn.commit()

            if cursor.rowcount > 0:
                print("Prix modifié avec succès.")
            else:
                print("Produit introuvable.")

        except sqlite3.Error as e:
            print("Erreur :", e)

    def fermer(self):
        self.conn.close()
