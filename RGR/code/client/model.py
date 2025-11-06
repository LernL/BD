import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=postgres user=postgres password=1234adminL host=localhost port=5432")
        self.conn.autocommit = True
        self.create_table()

    def create_table(self):
        with self.conn.cursor() as c:
            c.execute("""
            CREATE TABLE IF NOT EXISTS client (
                email varchar(30),
                phone_num_cl integer NOT NULL PRIMARY KEY,
                phone_num_w integer NOT NULL
            );
            """)
        self.conn.commit()

    def add(self, phone_num_cl, email, phone_num_w):
        with self.conn.cursor() as c:
            c.execute("INSERT INTO client (phone_num_cl, email, phone_num_w) VALUES (%s,%s,%s)",
                      (int(phone_num_cl), email, int(phone_num_w)))
        self.conn.commit()

    def list_all(self):
        with self.conn.cursor() as c:
            c.execute("SELECT phone_num_cl, email, phone_num_w FROM client ORDER BY phone_num_cl")
            return c.fetchall()

    def update(self, phone_num_cl, email, phone_num_w):
        with self.conn.cursor() as c:
            c.execute("UPDATE client SET email=%s, phone_num_w=%s WHERE phone_num_cl=%s",
                      (email, int(phone_num_w), int(phone_num_cl)))
        self.conn.commit()

    def delete(self, phone_num_cl):
        with self.conn.cursor() as c:
            c.execute("DELETE FROM client WHERE phone_num_cl=%s", (int(phone_num_cl),))
        self.conn.commit()

    def get_input(self):
        email = input("Email: ").strip()
        phone_num_w = input("Phone number waiter: ").strip()
        return email, phone_num_w

    def get_key(self):
        return input("Phone number client: ").strip()