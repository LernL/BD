import shutil


class View:

    def show_table(self, rows, cols, ms=None):
        if not rows:
            print("No data")
            return

        term_width = shutil.get_terminal_size((80, 20)).columns
        col_widths = [max(len(str(row[i])) for row in rows + [cols]) for i in range(len(cols))]

        def center_row(row):
            line = " | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row)))
            padding = max((term_width - len(line)) // 2, 0)
            return " " * padding + line

        # Друкуємо заголовок
        print(center_row(cols))
        print(center_row(["-" * w for w in col_widths]))

        # Друкуємо рядки
        for row in rows:
            print(center_row(row))

        # Друкуємо час виконання окремо, по центру всієї таблиці
        if ms is not None:
            total_width = sum(col_widths) + 3 * (len(cols) - 1)
            padding = max((term_width - total_width) // 2, 0)
            print(" " * padding + f"Time: {ms:.2f} ms")

    def get_input_int(self, prompt):
        s = input(prompt).strip()
        if s == "":
            return None
        if s.isdigit():
            return int(s)
        return None
