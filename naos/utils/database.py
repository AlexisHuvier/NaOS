import sqlite3


class Database:
    def __init__(self, fichier):
        self.connection = sqlite3.connect(fichier)
        self.cursor = self.connection.cursor()

    def executewithoutreturn(self, query, tuples=""):
        self.cursor = self.connection.cursor()
        if tuples == "":
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, tuples)
        self.connection.commit()

    def executewithreturn(self, query, tuples=""):
        self.cursor = self.connection.cursor()
        if tuples == "":
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, tuples)
        return self.cursor.fetchall()

    def reconnect(self, fichier):
        self.connection = sqlite3.connect(fichier)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def createdb(self):
        self.executewithoutreturn("""
CREATE TABLE IF NOT EXISTS parameters(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    background TEXT
)""")

        if not self.executewithreturn("""SELECT background FROM parameters"""):
            self.executewithoutreturn("""INSERT INTO parameters(background) VALUES(NULL)""")