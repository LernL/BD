from analytics.model import Model
from analytics.view import View
from mainview import MainView
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.mainview = MainView()
    def run(self):
        while True:
            choice = self.show_menu()
            if choice == '0':
                break
            elif choice == '1':
                self.by_table()
            elif choice == '2':
                self.by_waiter()
            elif choice == '3':
                self.show_table_bookings()
            else:
                self.mainview.show_message("Invalid choice")

    def show_menu(self):
        self.mainview.show_message("\nAnalytics: 1) By table/hour  2) By waiter  3) Show bookings for table  0) Back")
        return input("> ").strip()

    def by_table(self):
        ppl_min = self.view.get_input_int("people_num min (enter to skip): ")
        ppl_max = self.view.get_input_int("people_num max (enter to skip): ")
        hf = self.view.get_input_int("hour from (0-23, enter to skip): ")
        ht = self.view.get_input_int("hour to (0-23, enter to skip): ")
        tbl = self.view.get_input_int("num_table (enter to skip): ")

        rows, cols, ms = self.model.search_by_table(ppl_min, ppl_max, hf, ht, tbl)
        self.view.show_table(rows, cols, ms)

    def by_waiter(self):
        waiter = input("waiter name (partial, enter skip): ").strip()
        hf = self.view.get_input_int("hour from (0-23, enter to skip): ")
        ht = self.view.get_input_int("hour to (0-23, enter to skip): ")

        rows, cols, ms = self.model.search_by_waiter(waiter, hf, ht)
        self.view.show_table(rows, cols, ms)

    def show_table_bookings(self):
        tbl = self.view.get_input_int("num_table: ")
        if tbl is None:
            self.mainview.show_message("Invalid input")
            return
        rows, cols, ms = self.model.show_table_bookings(tbl)
        self.view.show_table(rows, cols, ms)
