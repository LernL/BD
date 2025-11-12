import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=postgres user=postgres password=1234adminL host=localhost port=5432")
        self.conn.autocommit = True
        self.create_table()

    def create_table(self):
        with self.conn.cursor() as c:
            c.execute("""
            CREATE TABLE IF NOT EXISTS contacts_client (
                email varchar NOT NULL PRIMARY KEY,
                name varchar
            );
            """)
        self.conn.commit()

    def add(self, email, name):
        with self.conn.cursor() as c:
            c.execute("INSERT INTO contacts_client(email, name) VALUES (%s,%s)", (email, name))
        self.conn.commit()

    def list_all(self):
        with self.conn.cursor() as c:
            c.execute("SELECT * FROM contacts_client ORDER BY email")
            return c.fetchall()

    def update(self, email, name):
        fields = []
        values = []

        if name != "":
            fields.append("name = %s")
            values.append(name)

        if not fields:
            return

        values.append(email)

        query = f"UPDATE contacts_client SET {', '.join(fields)} WHERE email = %s"

        with self.conn.cursor() as c:
            c.execute(query, values)

        self.conn.commit()

    def delete(self, email):
        with self.conn.cursor() as c:
            c.execute("DELETE FROM contacts_client WHERE email=%s", (email,))
        self.conn.commit()

    def get_input(self):
        name = input("Name: ").strip()
        return name

    def get_key(self):
        return input("Email: ").strip()