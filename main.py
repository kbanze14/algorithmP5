from Hotel import Hotel
from Attendee import Attendee
import random
import names
import math
import matplotlib.pyplot as plt


# cool function name i know
def do_project(attendee_a, hotels_h):
    # tried to use x but i had yellow underline that said matches outer scope
    # and we all know i cant have any yellow underlines
    # outer loop is going through each hotel name in the sorted list
    for q in attendee_a.sorted_hotel_list:
        # if the attendee is already in a hotel, break out of loop
        if attendee_a.current_hotel is not None:
            break
        else:
            # inner loop cycles through each hotel
            for y in hotels_h:
                # if the hotel 14 or less guests, then we can add a guest
                if y.num_guests < 15:
                    # if the outer loop hotel name matches the inner loop hotel name
                    # we add the guest, and give the guest a current hotel
                    # we then break out of loop
                    if q == y.h_name:
                        y.add_guest(attendee_a.name)
                        attendee_a.current_hotel = y.h_name
                        break
                else:
                    # if no num guests is 15 or more, go through next iteration of hotel
                    pass


# finding euclidean distance of guest to all hotels
def dist(attendee_a, hotels_h):
    for q in hotels_h:
        dist1 = math.sqrt(abs(attendee_a.x_val - q.hotel_x) + (abs(attendee_a.y_val - q.hotel_y)))
        # place in a dictionary, 'Hotel Kevin': 3.456
        attendee_a.hotel_list[q.h_name] = dist1
    # make sorted dictionary from unsorted dictionary
    attendee_a.sort_hotels(attendee_a.hotel_list, attendee_a.sorted_hotel_list)


if __name__ == '__main__':
    # list for hotels class
    hotels = []

    # list for x and y attendees and hotels for graph
    hotels_x = []
    hotels_y = []
    attendees_x = []
    attendees_y = []

    # creating 20 of hotels
    for x in range(20):
        hotels.append(Hotel(random.randint(0, 200), random.randint(0, 200), 0, [], 'Hotel ' + names.get_first_name(gender='female')))

    # creating 150 of attendees
    attendees = []
    for x in range(150):
        attendees.append(Attendee(random.randint(0, 200), random.randint(0, 200), names.get_first_name(gender='male'), {}, {}, None))

    # append x and y vals for hotels
    for x in hotels:
        hotels_x.append(x.hotel_x)
        hotels_y.append(x.hotel_y)

    # append x and y for attendees
    for x in attendees:
        attendees_x.append(x.x_val)
        attendees_y.append(x.y_val)

    # plotting the values and making titles for axes/legend
    plt.scatter(hotels_x, hotels_y, s=80, color='red', label='Hotels')
    plt.scatter(attendees_x, attendees_y, s=25, color='black', label="Attendees")
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.title('Hotel and Attendee Locations')
    plt.legend(bbox_to_anchor=(0.75, 1))
    plt.show()

    # getting distance of all attendees to hotels
    for x in attendees:
        dist(x, hotels)
    # placing attendees in hotels
    for x in attendees:
        do_project(x, hotels)

    # displaying hotel names and all guests
    for x in hotels:
        print(x.h_name)
        print(x.num_guests)
        print(x.guests)
