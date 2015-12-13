import dbConnection


def add_facebook_user(reflink, facebookId):
    conn = dbConnection.connect_to_database()
    if conn.execute("INSERT INTO facebook_user (LICZBA_OSOB_Z_POLECENIA, REFLINK, FACEBOOK_ID) VALUE (0, ?, ?)", (reflink, facebookId)):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False


def inc_liczba_osob_z_polecenia(facebookId):
    conn = dbConnection.connect_to_database()
    ilosc_osob = conn.execute("SELECT LICZBA_OSOB_Z_POLECENIA FROM facebook_user where FACEBOOK_ID = ?", (facebookId,))
    ilosc_osob += 1
    conn.execute("UPDATE facebook_user SET LICZBA_OSOB_Z_POLECENIA = ?", (ilosc_osob,))
    dbConnection.commit(conn)
    return True

def remove_facebook_user(facebookId):
    conn = dbConnection.connect_to_database()
    if conn.execute("DELETE FROM facebook_user where FACEBOOK_ID = ?", (facebookId,)):
        dbConnection.commit(conn)
        return True
    else:
        dbConnection.rollback(conn)
        return False