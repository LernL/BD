import shutil

class View:

    def show_table(self, rows, cols, ms=None):
        if not rows:
            print("No data")
            return

        term_width = shutil.get_terminal_size((80, 20)).columns
        n_cols = len(cols)
        col_width = max(term_width // n_cols - 3, 5)

        def format_row(row):
            return " | ".join(str(row[i] if row[i] is not None else "").ljust(col_width)[:col_width] for i in range(len(row)))

        header = format_row(cols)
        sep = "-".ljust(len(header), "-")

        print(header)
        print(sep)

        for row in rows:
            print(format_row(row))

        if ms is not None:
            print(f"\nTime: {ms:.2f} ms")

    def get_input_int(self, prompt):
        s = input(prompt).strip()
        if s == "":
            return None
        if s.isdigit():
            return int(s)
        return None
