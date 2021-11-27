class Attendee:
    # def __init__(self, name,  attendee_location_x, attendee_location_y, hotel_x, hotel_y, hotel_name, hotel_pref, hotel_names_pref):
    #     self.name = name
    #     self.attendee_location_x = attendee_location_x
    #     self.attendee_location_y = attendee_location_y
    #     self.hotel_x = hotel_x
    #     self.hotel_y = hotel_y
    #     self.hotel_name = hotel_name
    #     self.hotel_pref = hotel_pref
    #     self.hotel_names_pref = hotel_names_pref
    #
    # def print_guest(self):
    #     print('Attendee Name: ' + self.name)
    #     print('Attendee location: ' + str(self.attendee_location_x) + ', ' + str(self.attendee_location_y))
    #     if self.hotel_name != '':
    #         print('Hotel staying at: ' + self.hotel_name)
    #     else:
    #         print('Not at a hotel yet')
    #
    # def sort_prefs(self):
    #     self.hotel_pref.sort()
    #
    # def set_hotel_name(self, name):
    #     self.hotel_name = name

    def __init__(self, x_val, y_val, name, hotel_list, sorted_hotel_list, current_hotel):
        self.x_val = x_val
        self.y_val = y_val
        self.name = name
        self.hotel_list = hotel_list
        self.sorted_hotel_list = sorted_hotel_list
        self.current_hotel = current_hotel

    def sort_hotels(self, hotel_list, sorted_hotel_list):
        sorted_keys = sorted(hotel_list, key=hotel_list.get)
        for x in sorted_keys:
            sorted_hotel_list[x] = hotel_list[x]
