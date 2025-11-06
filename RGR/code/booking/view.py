class View:
    def __init__(self):
        self.cols = ["Initial booking time", "Final booking time", "Table number", "Number of people", "Id"]

    def show_items(self):
        sep = "-" * (3*25)
        print(sep)
        header_cells = [self.cols[i].center(25) for i in range(len(self.cols))]
        header = " | ".join(header_cells)
        print(header)

    def get_cols(self):
        return self.cols
