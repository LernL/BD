from booking.model import Model
from booking.view import View
from mainview import MainView

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.mainview = MainView()

    def run(self):
        while True:
            print("\nBookings: 1) Add 2) List 3) Update 4) Delete 0) Back")
            c = input("> ").strip()
            if c == '0': break
            if c == '1': self.add()
            elif c == '2': self.list()
            elif c == '3': self.update()
            elif c == '4': self.delete()
            else: print("Invalid")

    def add(self):
        time_b, end_t, num_table, phone, people_num = self.model.get_input()
        id = self.model.get_key()
        try:
            self.model.add(time_b, end_t, num_table, phone, people_num, id)
            self.mainview.show_message("Added.")
        except Exception as e:
            self.mainview.show_message(f"Error: {e}")

    def list(self):
        rows = self.model.list_all()
        self.view.show_items()
        cols = ["Initial booking time", "Final booking time", "Table number", "Number of people", "Id"]
        self.mainview.show_items(rows, cols)

    def update(self):
        id = self.model.get_key()
        time_b, end_t, num_table, phone, people_num = self.model.get_input()
        try:
            self.model.update(id, time_b, end_t, num_table, phone, people_num)
            self.mainview.show_message("Updated.")
        except Exception as e:
            self.mainview.show_message(f"Error: {e}")

    def delete(self):
        id = self.model.get_key()
        try:
            self.model.delete(id)
            self.mainview.show_message("Deleted.")
        except Exception as e:
            self.mainview.show_message(f"Error: {e}")
