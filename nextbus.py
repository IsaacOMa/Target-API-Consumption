

import sys
import requests
import time


def get_route_id():
    file1 = open("routes.txt", "r")
    arr = []
    line = "tmp"
    while line != "":
        line = file1.readline()
        arr.append(line.split(','))

    for x in arr:
        try:
            if sys.argv[1] in x[3] or sys.argv[1] in x[4]:
                return x[0]
        except IndexError:
            print("Error: invalid bus route input")
            sys.exit(1)

    return -1


def get_direction_id(route_id):
    r = requests.get('https://svc.metrotransit.org/nextripv2/directions/' + route_id)
    resp = r.json()
    # print(resp)
    for x in resp:
        try:
            if sys.argv[3] in x["direction_name"].lower():
                return x["direction_id"]  # returns the direction id
        except IndexError:
            print("Error: missing direction name")
            sys.exit(1)
    return -1


def get_stop_id(route_id, direction_id):
    r = requests.get('https://svc.metrotransit.org/nextripv2/stops/' + route_id + '/' + str(direction_id))
    resp = r.json()
    for x in resp:
        try:
            if sys.argv[2].lower() in x["description"].lower():
                return x["place_code"]
        except IndexError:
            print("Error: invalid bus stop name")
            sys.exit(1)
    return -1


def get_time_left(route_id, direction_id, place_code):
    r = requests.get('https://svc.metrotransit.org/nextripv2/' + route_id + '/' + str(direction_id) + '/' + place_code)
    resp = r.json()
    try:
        time_left = resp['departures'][0]['departure_time']
    except IndexError:
        print("The last bus has departed")
        sys.exit(1)

    time_left -= int(time.time())
    return time_left


def main():
    route_id = get_route_id()
    if route_id == -1:
        print("Error: bus route not found")
        sys.exit(1)

    direction_id = get_direction_id(route_id)
    if direction_id == -1:
        print("Error: direction not found")
        sys.exit(1)

    place_code = get_stop_id(route_id, direction_id)
    if place_code == -1:
        print("Error: bus stop destination not found")
        sys.exit(1)

    time_left = get_time_left(route_id, direction_id, place_code)
    time_remaining = int(time_left / 60)
    if time_left % 60 >= 30:
        time_remaining += 1
    print(str(time_remaining) + " Minutes")

    # print(time)
    # print(place_code)
    # print(direction_id)
    # (route_id)





if __name__ == '__main__':
    main()