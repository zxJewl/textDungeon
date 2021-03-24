import sqlite3
import script1

class Database:

    def __init__(self):
        self.conn=sqlite3.connect("files/inventory.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, item text, amount integer)")
        self.conn.commit()

    #comand to insert items
    def insert(self, item, amount):
        #test to see if item exists
        self.cur.execute("Select * from inventory where item = ?", (item, ))
        test=self.cur.fetchall()
        #if it does not, create a new entry for said item
        if len(test)==0:
            self.cur.execute("INSERT INTO inventory VALUES (NULL, ?,?)", (item,amount))
        #if it does exist, update amount
        else:
            self.cur.execute("SELECT * FROM inventory WHERE item=?", (item, ))
            am=self.cur.fetchall() 
            print(am[0][2]+amount)
            am=am[0][2]+amount
            print(am)
            self.cur.execute("UPDATE inventory SET amount=? WHERE item=?",(am,item))
        self.conn.commit()
        script1.viewINV()
        
    def delete(self, id):
        self.cur.execute("DELETE FROM inventory WHERE item=?",(id,))
        print("deleted: %s" % (id))
        self.conn.commit()
        script1.viewINV()

    def view(self):
        self.cur.execute("SELECT * FROM inventory")
        rows=self.cur.fetchall()
        return rows

    def search(self, title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall() 
        return rows



    def update(self, id, title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()