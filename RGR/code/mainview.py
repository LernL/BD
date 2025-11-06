import math

class MainView:
    def __init__(self):
        self.page_size = 100

    def show_items(self, rows, cols):
        sep = "-" * (len(cols)*25)
        printable_rows = []
        for r in rows:
            cells = []
            for i in range(len(cols)):
                text = "" if r[i] is None else str(r[i])
                cell = str(text).ljust(25)
                cells.append(cell)
            printable_rows.append(" | ".join(cells))

        total = len(printable_rows)
        pages = math.ceil(total / self.page_size)
        for p in range(pages):
            start = p * self.page_size
            end = start + self.page_size
            chunk = printable_rows[start:end]

            print(sep)
            for line in chunk:
                print(line)
            print(sep)


            shown = min(end, total)
            print(f"\nShowing {start+1}-{shown} of {total}. Page {p+1}/{pages}.")
            if shown == total:
                break

            cmd = input("[Enter] next, q quit: ").strip().lower()
            if cmd == "q":
                break

    def show_message(self, msg):
        print(msg)
