class Restaurant:
    def make_reservation(self, party_size):
        print(f'Booked table for {party_size}.')


class Steakhouse(Restaurant):
    pass


class Bar():
    def make_reservation(self, party_size):
        print(f'Booked a launge for {party_size}.')


class BarAndGrill(Steakhouse, Bar):
    pass


bar_and_grill=BarAndGrill()
bar_and_grill.make_reservation(4)