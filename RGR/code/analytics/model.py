import psycopg2
import time
class Model:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=postgres user=postgres password=1234adminL host=localhost port=5432")

    def search_by_table(self, people_min=None, people_max=None, hour_from=None, hour_to=None, num_table=None, limit=1000):
        where = []
        params = []
        if people_min is not None:
            where.append("b.people_num >= %s"); params.append(int(people_min))
        if people_max is not None:
            where.append("b.people_num <= %s"); params.append(int(people_max))
        if hour_from is not None:
            where.append("b.time_book >= %s"); params.append(int(hour_from))
        if num_table is not None:
            where.append("b.num_table = %s"); params.append(int(num_table))

        where_clause = ("WHERE " + " AND ".join(where)) if where else ""
        having_clause = "HAVING MAX(b.end_time) <= %s" if hour_to is not None else ""

        q = f"""
        SELECT
          t.num_table,
          t.table_shape,
          t.material,
          MIN(b.time_book) AS start_hour,
          MAX(b.end_time) AS end_hour,
          ROUND(AVG(b.people_num))::int AS avg_people
        FROM booking b
        JOIN "table" t ON b.num_table = t.num_table
        {where_clause}
        GROUP BY t.num_table, t.table_shape, t.material
        {having_clause}
        ORDER BY start_hour, t.num_table
        LIMIT %s
        """

        exec_params = list(params)
        if hour_to is not None:
            exec_params.append(int(hour_to))
        exec_params.append(int(limit))

        with self.conn.cursor() as cur:
            t0 = time.perf_counter()
            cur.execute(q, tuple(exec_params))
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description] if cur.description else []
            ms = (time.perf_counter() - t0) * 1000.0
        return rows, cols, ms

    def search_by_waiter(self, waiter_like=None, hour_from=None, hour_to=None, limit=1000):
        where = []
        params = []
        if waiter_like is not None:
            where.append("w.name ILIKE %s"); params.append(waiter_like)
        if hour_from is not None:
            where.append("b.time_book >= %s"); params.append(int(hour_from))

        where_clause = ("WHERE " + " AND ".join(where)) if where else ""
        having_clause = "HAVING MAX(b.end_time) <= %s" if hour_to is not None else ""

        q = f"""
        SELECT
          w.name AS waiter_name,
          MIN(b.time_book) AS start_hour,
          MAX(b.end_time) AS end_hour,
          SUM(b.people_num) AS total_people,
          ROUND(AVG(b.people_num))::int AS avg_people
        FROM booking b
        JOIN "table" t ON b.num_table = t.num_table
        LEFT JOIN client c ON b.phone_num_cl = c.phone_num_cl
        LEFT JOIN waiter w ON c.phone_num_w = w.phone_num_w
        {where_clause}
        GROUP BY w.name
        {having_clause}
        ORDER BY start_hour, w.name
        LIMIT %s
        """

        exec_params = list(params)
        if hour_to is not None:
            exec_params.append(int(hour_to))
        exec_params.append(int(limit))

        with self.conn.cursor() as cur:
            t0 = time.perf_counter()
            cur.execute(q, tuple(exec_params))
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description] if cur.description else []
            ms = (time.perf_counter() - t0) * 1000.0
        return rows, cols, ms

    def show_table_bookings(self, num_table, limit=1000):
        q = """
        SELECT
          b.id,
          b.time_book AS start_hour,
          b.end_time AS end_hour,
          b.phone_num_cl,
          c.email,
          co.name AS contact_name,
          w.name AS waiter_name,
          b.people_num
        FROM booking b
        LEFT JOIN client c ON b.phone_num_cl = c.phone_num_cl
        LEFT JOIN contacts_client co ON c.email = co.email
        LEFT JOIN waiter w ON c.phone_num_w = w.phone_num_w
        WHERE b.num_table = %s
        ORDER BY b.time_book, b.id
        LIMIT %s
        """
        with self.conn.cursor() as cur:
            t0 = time.perf_counter()
            cur.execute(q, (int(num_table), int(limit)))
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description] if cur.description else []
            ms = (time.perf_counter() - t0) * 1000.0
        return rows, cols, ms
