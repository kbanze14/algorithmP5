class Hotel:
    # def __init__(self, hotel_location_x, hotel_location_y, num_guests, attendee, name):
    #     self.hotel_location_x = hotel_location_x
    #     self.hotel_location_y = hotel_location_y
    #     self.num_guests = num_guests
    #     self.attendee = attendee
    #     self.name = name
    #
    # def add_attendee(self, g):
    #     if self.num_guests < 15:
    #         self.num_guests += 1
    #         self.attendee.append(g)
    #
    # def print_hlocation(self):
    #     print(self.name)
    #     print('Location: ' + str(self.hotel_location_x) + ', ' + str(self.hotel_location_y))
    #
    def __init__(self, hotel_x, hotel_y, num_guests, guests, h_name):
        self.hotel_x = hotel_x
        self.hotel_y = hotel_y
        self.num_guests = num_guests
        self.guests = guests
        self.h_name = h_name

    def add_guest(self, guest_name):
        self.guests.append(guest_name)
        self.num_guests += 1
