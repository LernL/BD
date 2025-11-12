class View:
    def __init__(self):
        self.cols = ["Name", "Employee number"]

    def show_items(self):
        sep = "-" * (2*25)
        print(sep)
        header_cells = [self.cols[i].center(25) for i in range(len(self.cols))]
        header = " | ".join(header_cells)
        print(header)
