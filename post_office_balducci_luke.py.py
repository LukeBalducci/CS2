"""
Author: Luke Balducci
sources: Mr. Campbell, assaignmentsheet
description: will take the dimensions and zipcode information and will return a ocde
date: 10.23.2025
bugs: only works whit commas in between

"""

def get_dimensions(length, width, height):
    try:
        length = float(length)
        width = float(width)
        height = float(height)
    except:
        return "unmailable"
    # used to get what package type 
    # uses numbers instead of names to reduce possible error in spelling and for simplicity 
    if 3.5 <= length <= 4.25 and 0.007 <= width <= 0.016 and 3.5 <= height <= 6:
        return "1"
    elif 4.25 <= length <= 6 and 0.007 <= width <= 0.015 and 6 <= height <= 11.5:
        return "2"
    elif 3.5 <= length <= 6.125 and 0.016 <= width <= 0.25 and 5 <= height <= 11.5:
        return "3"
    elif 6.125 <= length <= 24 and 0.25 <= width <= 0.5 and 11 <= height <= 18:
        return "4"
    elif (length > 24 or width > 0.5 or height > 18) and (length + 2 * (width + height) < 84):
        return "5"
    elif (length > 24 or width > 0.5 or height > 18) and (84 <= length + 2 * (width + height) < 130):
        return "6"
    else:
        return "unmailable"


def get_zip_zone(zip1, zip2):
    # use one if/elif set to find both zones
    def find_zone(zipcode):
        if 1 <= zipcode <= 6999:
            return 1
        elif 7000 <= zipcode <= 19999:
            return 2
        elif 20000 <= zipcode <= 35999:
            return 3
        elif 36000 <= zipcode <= 62999:
            return 4
        elif 63000 <= zipcode <= 84999:
            return 5
        elif 85000 <= zipcode <= 99999:
            return 6
        else:
            return -1
    
    zone1 = find_zone(zip1)
    zone2 = find_zone(zip2)
    
    if zone1 == -1 or zone2 == -1:
        return -1
    # find the distance between the 2 zones and if negative uses ablsolute value
    return abs(zone1 - zone2)


def get_cost(package_class, zone_distance):
    if package_class == "unmailable" or zone_distance < 0:
        return "unmailable"
 # calculates shipping cost bases on distance and package class
    if package_class == "1":
        base, extra = 0.20, 0.03
    elif package_class == "2":
        base, extra = 0.37, 0.03
    elif package_class == "3":
        base, extra = 0.37, 0.04
    elif package_class == "4":
        base, extra = 0.60, 0.05
    elif package_class == "5":
        base, extra = 2.95, 0.25
    elif package_class == "6":
        base, extra = 3.95, 0.35
    else:
        return "unmailable"
    # multiplys "extra" by the zone distance to get accurate tax
    total = base + (zone_distance * extra)
    return round(total, 2)


def main():
    user_input = input("Enter info in this specific order using only numbers and commas to seperate data (length,height,width,zip_from,zip_to): ")

    # split by comma instead 
    data = user_input.split(",")
    if len(data) != 5:
        print("Error: Please enter exactly 5 values separated by commas.")
        return
    # user must put commas inbetween information
    try:
        length = float(data[0])
        height = float(data[1])
        width = float(data[2])
        zip1 = int(data[3])
        zip2 = int(data[4])
    except:
        print("error, only numbers excepted .")
        return

    package_class = get_dimensions(length, width, height)
    zone_distance = get_zip_zone(zip1, zip2)
    total_cost= get_cost(package_class, zone_distance)

    print( total_cost)



main() 

