class Hotel:

    # hotel class, pretty self explanatory
    def __init__(self, hotel_x, hotel_y, num_guests, guests, h_name):
        self.hotel_x = hotel_x
        self.hotel_y = hotel_y
        self.num_guests = num_guests
        self.guests = guests
        self.h_name = h_name

    def add_guest(self, guest_name):
        self.guests.append(guest_name)
        self.num_guests += 1
