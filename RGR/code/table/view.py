class View:
    def __init__(self):
        self.cols = ["Table number", "Number of chairs", "Material", "Table shape"]

    def show_items(self):
        sep = "-" * (4*25)
        print(sep)
        header_cells = [self.cols[i].center(25) for i in range(len(self.cols))]
        header = " | ".join(header_cells)
        print(header)

    def get_cols(self):
        return self.cols
