import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=postgres user=postgres password=1234adminL host=localhost port=5432")
        self.conn.autocommit = True
        self.create_table()

    def create_table(self):
        with self.conn.cursor() as c:
            c.execute("""
            CREATE TABLE IF NOT EXISTS waiter (
                name varchar(20) NOT NULL,
                phone_num_w integer NOT NULL PRIMARY KEY,
                UNIQUE (name)
            );
            """)
        self.conn.commit()

    def add(self, phone_num_w, name):
        with self.conn.cursor() as c:
            c.execute("INSERT INTO waiter (phone_num_w, name) VALUES (%s,%s)", (int(phone_num_w), name))
        self.conn.commit()

    def list_all(self):
        with self.conn.cursor() as c:
            c.execute("SELECT * FROM waiter ORDER BY phone_num_w")
            return c.fetchall()

    def update(self, phone_num_w, new_name):
        fields = []
        values = []

        if new_name != "":
            fields.append("name = %s")
            values.append(new_name)

        if not fields:
            return

        values.append(int(phone_num_w))

        query = f"UPDATE waiter SET {', '.join(fields)} WHERE phone_num_w = %s"

        with self.conn.cursor() as c:
            c.execute(query, values)

        self.conn.commit()

    def delete(self, phone_num_w):
        with self.conn.cursor() as c:
            c.execute("DELETE FROM waiter WHERE phone_num_w=%s", (int(phone_num_w),))
        self.conn.commit()

    def get_input(self):
        name = input("Name: ").strip()
        return name

    def get_key(self):
        return input("Phone number: ").strip()

