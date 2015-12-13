import dbConnection


def add_zdjecie(hash, organizacjaId):
    conn = dbConnection.connect_to_database()
    if conn.execute("INSERT INTO ZDJECIE (B64_HASH, ORGANIZACJA_ID) VALUE (?, ?)", (hash, organizacjaId)):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def remove_umiejetnosc(organizacjaId):
    conn = dbConnection.connect_to_database()
    if conn.execute("DELETE FROM ZDJECIE WHERE ORGANIZACJA_ID = ?", (organizacjaId,)):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False
