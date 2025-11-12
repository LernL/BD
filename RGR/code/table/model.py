import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=postgres user=postgres password=1234adminL host=localhost port=5432")
        self.conn.autocommit = True
        self.create_table()

    def create_table(self):
        with self.conn.cursor() as c:
            c.execute("""
            CREATE TABLE IF NOT EXISTS public.table
            (
                num_table integer NOT NULL,
                number_chairs integer,
                material character varying(20),
                table_shape character varying(20),
                PRIMARY KEY (num_table)
            );
            """)
        self.conn.commit()

    def add(self, num_table, number_chairs, material, table_shape):
        with self.conn.cursor() as c:
            c.execute('INSERT INTO public.table (num_table, number_chairs, material, table_shape) VALUES (%s,%s,%s,%s)',
                      (int(num_table), int(number_chairs) if number_chairs != "" else None, material or None, table_shape or None))
        self.conn.commit()

    def list_all(self):
        with self.conn.cursor() as c:
            c.execute('SELECT * FROM public.table ORDER BY num_table')
            return c.fetchall()

    def update(self, num_table, number_chairs, material, table_shape):
        fields = []
        values = []

        if number_chairs != "":
            fields.append("number_chairs = %s")
            values.append(int(number_chairs))

        if material != "":
            fields.append("material = %s")
            values.append(material)

        if table_shape != "":
            fields.append("table_shape = %s")
            values.append(table_shape)

        if not fields:
            return

        values.append(int(num_table))

        query = f"UPDATE public.table SET {', '.join(fields)} WHERE num_table = %s"

        with self.conn.cursor() as c:
            c.execute(query, values)

        self.conn.commit()

    def delete(self, num_table):
        with self.conn.cursor() as c:
            c.execute('DELETE FROM public.table WHERE num_table=%s', (int(num_table),))
        self.conn.commit()

    def get_input(self):
        number_chairs = input("Number of chairs: ").strip()
        material = input("Material: ").strip()
        table_shape = input("Shape of table: ").strip()
        return number_chairs, material, table_shape

    def get_key(self):
        return input("Id: ").strip()