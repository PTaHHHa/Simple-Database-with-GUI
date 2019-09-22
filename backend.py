import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Libriary (id INTEGER PRIMARY KEY, title text, author text, year integer, "
            "isbn integer)")
        self.conn.commit()

    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO Libriary VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM Libriary")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM Libriary WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM Libriary WHERE id=?", (id,))
        self.conn.commit()


    def update(self,id, title, author, year, isbn):
        self.cur.execute("UPDATE Libriary SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def clear(self):
        self.cur.execute("DELETE FROM Libriary")
        self.conn.commit()


    def __del__(self):
        self.conn.close()