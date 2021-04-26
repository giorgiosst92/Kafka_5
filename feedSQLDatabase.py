from sqlConnection import create_connection
from random import randint


database = r"pythonsqlite.db"

conn = create_connection(database)

def create_project(conn, values):
    """
    Create a new user into the user table
    :param conn:
    :param values:
    :return: userId
    """
    sql = ''' INSERT INTO user(userId,ads_count)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    return cur.lastrowid


if __name__ == '__main__':

    for i in range(2,101):
        values = (i,randint(0, 150))

        create_project(conn,values)