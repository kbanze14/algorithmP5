class Attendee:

    # attendee class has 2 dictionaries, one that goes populates in the order that the hotels are created
    # other one sorted by distance
    def __init__(self, x_val, y_val, name, hotel_list, sorted_hotel_list, current_hotel):
        self.x_val = x_val
        self.y_val = y_val
        self.name = name
        self.hotel_list = hotel_list
        self.sorted_hotel_list = sorted_hotel_list
        self.current_hotel = current_hotel

    # sorts the dictionary and populates the sorted dictionary
    # this is used for when we add guests to hotels
    def sort_hotels(self, hotel_list, sorted_hotel_list):
        sorted_keys = sorted(hotel_list, key=hotel_list.get)
        for x in sorted_keys:
            sorted_hotel_list[x] = hotel_list[x]
