from kafka import KafkaProducer
from sqlConnection import create_connection


database = r"pythonsqlite.db"

conn = create_connection(database)


def from_sqlite_to_kafka(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")

    rows = cur.fetchall()

    for row in rows:
        
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        producer.send('virtual-mind', str(row).encode('utf-8'))

    producer.flush()


from_sqlite_to_kafka(conn)