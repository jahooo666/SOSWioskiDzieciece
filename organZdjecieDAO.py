import dbConnection


def add_organizacja_zdjecie_relation(organizacjaId, zdjecieId):
    conn = dbConnection.connect_to_database()
    params = (organizacjaId, zdjecieId)
    if conn.execute("INSERT INTO ORGAN_ZDJECIE (ORGANIZACJA_ID, ZDJECIE_ID) VALUE (?, ?)", params):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def remove_zdjecie_by_organizacja_id(organizacjaId):
    conn = dbConnection.connect_to_database()
    if conn.execute("DELETE FROM ORGAN_ZDJECIE WHERE ORGANIZACJA_ID = ?", (organizacjaId,)):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False
