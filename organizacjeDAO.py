import dbConnection


def add_organizacja(nazwa, email, nrKrs):
    conn = dbConnection.connect_to_database()
    if conn.execute("INSERT INTO organizacje (NAZWA, EMAIL, NR_KRS, CZY_POTWIERDZONY) VALUE (?, ?, ?, 0)", (nazwa, email, nrKrs)):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def remove_organizacja(organizacjaId):
    conn = dbConnection.connect_to_database()
    if conn.execute("DELETE FROM organizacje WHERE ID = ?", (organizacjaId,)):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False

def set_organizacja_potwierdzona(organizacjaId):
    conn = dbConnection.connect_to_database()
    if conn.execute("UPDATE organizacje SET CZY_POTWIERDZONY = ?", 1):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False
