class MainController:
    def mainmenu(self):
        while True:
            print("\nMain menu: 1) Waiters 2) Clients 3) Tables 4) Bookings 5) Contacts 6) Analytics 0) Exit")
            choice = input("> ").strip()

            if choice == '0':
                break
            elif choice == '1':
                from waiter.controller import Controller as WaiterCtrl
                WaiterCtrl().run()
            elif choice == '2':
                from client.controller import Controller as ClientCtrl
                ClientCtrl().run()
            elif choice == '3':
                from table.controller import Controller as TableCtrl
                TableCtrl().run()
            elif choice == '4':
                from booking.controller import Controller as BookingCtrl
                BookingCtrl().run()
            elif choice == '5':
                from contacts_client.controller import Controller as ContactsCtrl
                ContactsCtrl().run()
            elif choice == '6':
                from analytics.controller import Controller as AnalyticsCtrl
                AnalyticsCtrl().run()
            else:
                print("Invalid choice")