import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=postgres user=postgres password=1234adminL host=localhost port=5432")
        self.conn.autocommit = True
        self.create_table()

    def create_table(self):
        with self.conn.cursor() as c:
            c.execute("""
            CREATE TABLE IF NOT EXISTS booking (
                time_book integer NOT NULL,
                end_time integer NOT NULL,
                num_table integer NOT NULL,
                phone_num_cl integer NOT NULL,
                people_num integer,
                id integer NOT NULL PRIMARY KEY,
                UNIQUE (time_book, num_table)
            );
            """)
        self.conn.commit()

    def add(self, time_book, end_time, num_table, phone_num_cl, people_num, id_pk):
        with self.conn.cursor() as c:
            c.execute("INSERT INTO booking (time_book,end_time,num_table,phone_num_cl,people_num,id) VALUES (%s,%s,%s,%s,%s,%s)",
                      (int(time_book), int(end_time), int(num_table), int(phone_num_cl), int(people_num), int(id_pk)))
        self.conn.commit()

    def list_all(self):
        with self.conn.cursor() as c:
            c.execute("SELECT * FROM booking ORDER BY id")
            return c.fetchall()

    def update(self, id, time_book, end_time, num_table, phone_num_cl, people_num):
        fields = []
        values = []

        if time_book != "":
            fields.append("time_book = %s")
            values.append(int(time_book))

        if end_time != "":
            fields.append("end_time = %s")
            values.append(int(end_time))

        if num_table != "":
            fields.append("num_table = %s")
            values.append(int(num_table))

        if phone_num_cl != "":
            fields.append("phone_num_cl = %s")
            values.append(int(phone_num_cl))

        if people_num != "":
            fields.append("people_num = %s")
            values.append(int(people_num))

        if not fields:
            return

        values.append(int(id))

        query = f"UPDATE booking SET {', '.join(fields)} WHERE id = %s"

        with self.conn.cursor() as c:
            c.execute(query, values)

        self.conn.commit()
    def delete(self, id_pk):
        with self.conn.cursor() as c:
            c.execute("DELETE FROM booking WHERE id=%s", (int(id_pk),))
        self.conn.commit()

    def get_input(self):
        time_book = input("Initial booking time: ").strip()
        final_time = input("Final booking time: ").strip()
        num_table = input("Table number: ").strip()
        phone = input("Phone number client: ").strip()
        num_people = input("Number of people: ").strip()
        return time_book, final_time, num_table, phone, num_people
    def get_key(self):
        return input("Id: ").strip()