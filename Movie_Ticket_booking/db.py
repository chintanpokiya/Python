import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS tickets(
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            contact TEXT,
            movie_name TEXT,
            movie_prize TEXT,
            movie_type TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, email, contact, movie_name, movie_prize, movie_type):
        self.cur.execute("INSERT INTO tickets VALUES (NULL,?,?,?,?,?,?)",
                         (name, email, contact, movie_name, movie_prize, movie_type))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * FROM tickets")
        rows = self.cur.fetchall()
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("DELETE FROM tickets WHERE id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, email, contact, movie_name, movie_prize, movie_type):
        self.cur.execute(
            "UPDATE tickets SET name=?, email=?, contact=?, movie_name=?, movie_prize=?, movie_type=? WHERE id=?",
            ( name, email, contact, movie_name, movie_prize, movie_type, id))
        self.con.commit()
