from client.model import Model
from client.view import View
from mainview import MainView
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.mainview = MainView()

    def run(self):
        while True:
            print("\nClients: 1) Add 2) List 3) Update 4) Delete 0) Back")
            c = input("> ").strip()
            if c == '0': break
            if c == '1': self.add()
            elif c == '2': self.list()
            elif c == '3': self.update()
            elif c == '4': self.delete()
            else: print("Invalid")

    def add(self):
        phone = self.model.get_key()
        email, waiter = self.model.get_input()
        try:
            self.model.add(phone, email, waiter)
            self.mainview.show_message("Added.")
        except Exception as e:
            self.mainview.show_message(f"Error: {e}")

    def list(self):
        rows = self.model.list_all()
        self.view.show_items()
        cols = ["Phone number client", "Email", "Phone number waiter"]
        self.mainview.show_items(rows, cols)

    def update(self):
        phone = self.model.get_key()
        email, waiter = self.model.get_input()
        try:
            self.model.update(phone, email, waiter)
            self.mainview.show_message("Updated.")
        except Exception as e:
            self.mainview.show_message(f"Error: {e}")

    def delete(self):
        phone = self.model.get_key()
        try:
            self.model.delete(phone)
            self.mainview.show_message("Deleted.")
        except Exception as e:
            self.mainview.show_message(f"Error: {e}")
