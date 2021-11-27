from Hotel import Hotel
from Attendee import Attendee
import random
import names
import math
#
#
# def distance(Hotel, Attendee, listy):
#     dist = math.sqrt(abs(Attendee.attendee_location_x - Hotel.hotel_location_x) + (abs(Attendee.attendee_location_y - Hotel.hotel_location_y)))
#     listy.append([dist, Hotel.name, Attendee.name])
#     return listy
#
#
# def hotel_names_list(pref_list, name_list):
#     for a in range(20):
#         name_list.append(pref_list[a][1])
#     return name_list
#
#
# if __name__ == '__main__':
#     # lists to store all information for making hotels & guests
#     # hotel location
#     x_list_hotels = []
#     y_list_hotels = []
#     # hotels
#     hotels = []
#     #attendees x and y
#     x_list_attend = []
#     y_list_attend = []
#     # attendees
#     attendees = []
#     # name generator list
#     hotel_names = []
#     # name generator list
#     attendee_names = []
#
#     # random name hen for hotels
#     for x in range(20):
#         hotel_names.append('Hotel ' + names.get_first_name(gender='female'))
#
#     # random name gen for attendees
#     for x in range(150):
#         attendee_names.append(names.get_full_name(gender='male'))
#
#     # populating hotel lists
#     for x in range(20):
#         x_list_hotels.append(random.randint(0, 200))
#         y_list_hotels.append(random.randint(0, 200))
#     for x in range(20):
#         hotels.append(Hotel(x_list_hotels[x], y_list_hotels[x], 0, [], hotel_names[x]))
#
#     # populating guest lists
#     for x in range(150):
#         x_list_attend.append(random.randint(0,200))
#         y_list_attend.append(random.randint(0, 200))
#     for x in range(150):
#         attendees.append(Attendee(attendee_names[x], x_list_attend[x], y_list_attend[x], None, None, '', [], []))
#     list1 = []
#
#     # Euclidean distance on each hotel
#     for x in attendees:
#         for y in hotels:
#             x.hotel_pref = distance(y, x, x.hotel_pref)
#     # sort the list of euclidean distances in order from clsoest to furthest
#     for x in attendees:
#         x.sort_prefs()
#         x.hotel_names_pref = hotel_names_list(x.hotel_pref, x.hotel_names_pref)
#
#     attendees[0].print_guest()
#     print(attendees[0].hotel_pref)
#     for x in hotels:
#         x.print_hlocation()


# try number 2
def do_project(attendee_a, hotels_h):
    for q in attendee_a.sorted_hotel_list:
        if attendee_a.current_hotel is not None:
            break
        else:
            for y in hotels_h:
                if y.num_guests < 16:
                    if q == y.h_name:
                        y.add_guest(attendee_a.name)
                        attendee_a.current_hotel = y.h_name
                        break
                else:
                    pass


def dist(attendee_a, hotels_h):
    for q in hotels_h:
        dist1 = math.sqrt(abs(attendee_a.x_val - q.hotel_x) + (abs(attendee_a.y_val - q.hotel_y)))
        attendee_a.hotel_list[q.h_name] = dist1
    attendee_a.sort_hotels(attendee_a.hotel_list, attendee_a.sorted_hotel_list)


if __name__ == '__main__':
    # list for hotels class
    hotels = []

    # creating list of hotels
    for x in range(20):
        hotels.append(Hotel(random.randint(0, 200), random.randint(0, 200), 0, [], 'Hotel ' + names.get_first_name(gender='female')))

    a = Attendee(random.randint(0,200), random.randint(0,200), names.get_first_name(gender='male'), {}, {}, None)
    attendees = []
    for x in range(150):
        attendees.append(Attendee(random.randint(0,200), random.randint(0,200), names.get_first_name(gender='male'), {}, {}, None))
    for x in hotels:
        distance = math.sqrt(abs(a.x_val - x.hotel_x) + (abs(a.y_val - x.hotel_y)))
        a.hotel_list[x.h_name] = distance

    print(a.hotel_list)
    a.sort_hotels(a.hotel_list, a.sorted_hotel_list)
    print(a.sorted_hotel_list)

    for x in attendees:
        dist(x, hotels)
        do_project(a, hotels)
    for x in hotels:
        print(x.h_name)
        print(x.num_guests)
        print(x.guests)

    # sorted_keys = sorted(a.hotel_list, key=a.hotel_list.get)
    # for x in sorted_keys:
    #     a.sorted_hotel_list[x] = a.hotel_list[x]
    # print(a.sorted_hotel_list)